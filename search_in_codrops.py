import sublime, sublime_plugin,webbrowser

class SearchInCodropsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #self.view.insert(edit, 0, "Voy a buscar en codrops!")
        url = 'http://tympanus.net/codrops/css_reference/'
        sel = self.view.sel()
        word = self.view.substr(sel[0])
        webbrowser.open_new_tab(url + word)