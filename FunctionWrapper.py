import sublime, sublime_plugin

class WrapFunctionCommand(sublime_plugin.TextCommand):
    PLACEHOLDER = "func"

    def run(self, edit):
        selection = self.view.sel()

        # Check if there is a selection
        for region in selection:
            if region.empty():
                sublime.message_dialog("Please select something.")
                return

        new_regions = []
        for region in selection:
            begin = self.PLACEHOLDER + "("
            self.view.insert(edit, region.end(), ")")
            self.view.insert(edit, region.begin(), begin)
            new_regions.append(sublime.Region(region.begin(), region.begin() + len(self.PLACEHOLDER)))


        selection.clear()
        selection.add_all(new_regions)
