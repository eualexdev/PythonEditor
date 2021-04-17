from PyQt5 import QtCore
from PyQt5.QtWidgets import QPlainTextEdit,QCompleter
from PyQt5.QtCore import QRect, QRegExp, Qt
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter, QTextCursor

def QSetStyles(r=0,g=0,b=0, style=''):
    # 

    _color_ = QColor()
    _color_.setRgb(r,g,b,100)

    _format_ = QTextCharFormat()
    _format_.setForeground(_color_)
    if 'bold' in style:
        _format_.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format_.setFontItalic(True)

    return _format_




class QCodeColors (QSyntaxHighlighter):
    #Syntax highlighter for language.
   
    def __init__(self, document,STYLES,keywords,operators,braces):
        QSyntaxHighlighter.__init__(self, document)

        self.tri_single = (QRegExp("'''"), 1, STYLES['string2'])
        self.tri_double = (QRegExp('"""'), 2, STYLES['string2'])
    
        self.rules = []

        self.rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
            for w in keywords]
        self.rules += [(r'%s' % o, 0, STYLES['operator'])
            for o in operators]
        self.rules += [(r'%s' % b, 0, STYLES['brace'])
            for b in braces]

        self.rules += [
            # (r'\bself\b', 0, STYLES['self']),


            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),

            # (r'\bdef\b\s*', 1, STYLES['']),
            # (r'\bclass\b\s*', 1, STYLES['ikeyword']),
            
            (r'#[^\n]*', 0, STYLES['comment']),
            
            (r'"', 0, STYLES['string']),
            (r"'", 0, STYLES['string']),

             (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
        ]

        self.finalRu = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in self.rules]


    def SetNewKeywordColor(self,key,color):
        self.rules += (r'\b'+key+r'\b', 0, color),
        self.finalRu = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in self.rules]


    def highlightBlock(self, text):
        for expression, nth, format in self.finalRu:
            index = expression.indexIn(text, 0)

            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)


    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        else:
            start = delimiter.indexIn(text)
            add = delimiter.matchedLength()

        while start >= 0:
            end = delimiter.indexIn(text, start + add)
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            self.setFormat(start, length, style)
            start = delimiter.indexIn(text, start + length)

        if self.currentBlockState() == in_state:
            return True
        else:
            return False



class QCodeCompleter(QCompleter):
    insertText = QtCore.pyqtSignal(str)
    def __init__(self, parent=None,keywords=[]):
        QCompleter.__init__(self, keywords, parent)
        self.setCompletionMode(QCompleter.PopupCompletion)
        self.highlighted.connect(self.setHighlighted)
        
    def setHighlighted(self, text):
        self.lastSelected = text + " "

    def getSelected(self):
        return self.lastSelected

class QCodeEdit(QPlainTextEdit):
    def __init__(self, parent=None,STYLES=[],keywords=[],operators=[],braces=[]):
        super(QCodeEdit, self).__init__(parent)

        self.completer = QCodeCompleter(keywords=keywords)
        self.completer.setWidget(self)
        self.completer.insertText.connect(self.__insertCompletion)
        self.keywordColor = QCodeColors(self.document(),STYLES,keywords,operators,braces)

    def __insertCompletion(self, completion):
        tc = self.textCursor()
        extra = (len(completion) - len(self.completer.completionPrefix()))
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)
        self.completer.popup().hide()

    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self)
        QPlainTextEdit.focusInEvent(self, event)

    def keyPressEvent(self, event):
    
        tc = self.textCursor()
        if event.key() == Qt.Key_Tab and self.completer.popup().isVisible():
            self.completer.insertText.emit(self.completer.getSelected())
            self.completer.setCompletionMode(QCompleter.PopupCompletion)
            return

        QPlainTextEdit.keyPressEvent(self, event)
        tc.select(QTextCursor.WordUnderCursor)
        cr = self.cursorRect()
        
        if len(tc.selectedText()) > 0:
            self.completer.setCompletionPrefix(tc.selectedText())
            popup = self.completer.popup()
            popup.setCurrentIndex(self.completer.completionModel().index(0,0))

            cr.setWidth(self.completer.popup().sizeHintForColumn(0) 
            + self.completer.popup().verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)
        else:
            self.completer.popup().hide()