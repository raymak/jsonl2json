import sublime, sublime_plugin

class JsonlToJsonCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		allcontent = sublime.Region(0, self.view.size())

		lineRegions = self.view.split_by_newlines(allcontent)

		lines = list(map(self.view.substr, lineRegions))

		out = "[" + ",\n".join(lines) + "]"

		self.view.replace(edit, allcontent, out)

		self.view.run_command("pretty_json")