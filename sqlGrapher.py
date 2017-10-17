import sublime
import sublime_plugin
import main as main
# import anltr4
import antlr4.LL1Analyzer

class sqlgragherCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# self.view.insert(edit, 0, self.view.file_name())
		path = self.view.file_name()
		# import antlr4.LL1Analyzer
		import antlr4.Lexer
		print path
		# self.view.insert(edit, 0, self.view.size())
		main.g(path)