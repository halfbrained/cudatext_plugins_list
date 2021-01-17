Name: ASCII Art  
Description: Inserts text formatted via ASCII art font (using PyFiglet)  
<details><summary>readme</summary>
```
Plugin "ASCII Art" for CudaText.
It gives command to render any text via ASCII Art font. Many fonts are available. Uses PyFiglet library.

For example, string "Test..." will be converted to:

  ______          __     
 /_  __/__  _____/ /_    
  / / / _ \/ ___/ __/    
 / / /  __(__  ) /__ _ _ 
/_/  \___/____/\__(_|_|_)

or, with another font:

 _____             _            
(_   _)           ( )_          
  | |   __    ___ | ,_)         
  | | /'__`\/',__)| |           
  | |(  ___/\__, \| |_  _  _  _ 
  (_)`\____)(____/`\__)(_)(_)(_)

Plugin has few commands in Plugins menu.
You can open config file using one of Plugins commands. Details:

- direction: possible values are 'auto', 'left-to-right', 'right-to-left'
- justify: possible values are 'auto' (inherit from direction), 'left', 'right'
- width: has effect when justify is 'right' 

Author: Alexey Torgashin (CudaText)
License: MIT

```</details>----------
   
   
Name: Auto Center Line  
Description: Plugin keeps current line in the center of the editor window  
<details><summary>readme</summary>
```
plugin for CudaText.
when active, it changes vertical scroll position, so that line 
with caret is always centered in the editor window.

plugin gives 2 commands in the menu Plugins - Auto Center Line:
- Activate (you must call it for plugin to work)
- Deactivate
plugin is not activated on CudaText restart.
plugin is passive when multi-carets are placed.

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: Auto-Copy to Clipboard  
Description: When text block selected, it's auto copied to clipboard, no need to press Ctrl+C (or call menu item). Don't work with multi-carets. Don't work for huge blocks (>50K).  
<details><summary>readme</summary>
```
plugin for CudaText.
on making text selection (with mouse, shift+arrows, ctrl+A, etc), copies selected block to clipboard.

- handles forward/backward selections.
- won't work with multi-carets.
- won't work for too big blocks (limit is 50K, it is option).
- won't handle vertical blocks.

plugin has config file, to call it, use menu item in "Options / Settings-plugins / Auto-Copy to Clipboard".

- min_len: min length of selection to handle.
- max_len: max length of selection to handle (to not freeze on huge block).
- copy_to_clipboard (0 or 1): auto-copy to usual clipboard.
    if you want to disable auto-copy to usual clipboard, set option to 0.
    this is good, if you don't want to overwrite usual clipboard with Auto-Copy, 
    and want Auto-Copy set only primary-sel buffer. then middle-click-paste 
    will paste from primary-sel buffer, and it's like in Linux apps.
- copy_to_primary_sel (0 or 1): auto-copy to primary-selection. 
    (alternate buffer in Linux GTK library, it's used by CudaText on middle-button-click, 
    and by other Linux editors too.)


author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: Auto Replace  
Description: Plugin auto-replaces currently typed words, based on set of snippets with such words.  
<details><summary>readme</summary>
```
plugin for CudaText.
allows to auto-replace keywords/functions, when they are typed in the wrong case (e.g. "writeln" to "WriteLn"). allows usual word replace too. you must create one or several snippet collection(s) in .cuda-dic format: one word per line, comments must begin with # char.

for ex, to replace words "readln" and "writeln" in lexer Pascal, create file "[CudaText dir]/data/autoreplace/pascal/mytest.cuda-dic" with contents:

WriteLn
ReadLn

word is replaced when user goes off this word: by Space, Tab, symbol chars, punctuation, Home/End, PageUp/PageDown, mouse click.

note that [CudaText dir] on Unix is "~/.cudatext".
note that you need subfolder in the lower case inside "data/autoreplace" folder.
plugin prints in the Console panel, that it actually has found some snippets, e.g. "Auto Replace: for all lexers: found Pascal[5]".
such snippet collections can be distributed as CudaText add-ons.
plugin gives configuration menu item(s): "Options / Settings-plugins / Auto Replace".

authors:
  Alexey T. (CudaText)
  Khomutov Roman (iRamSoft on Github)
license: MIT

```</details>----------
   
   
Name: Auto Save  
Description: Saves modified files automatically: before file closing (by option, default is off), by timer (default interval 30sec), on application deactivation  
<details><summary>readme</summary>
```
plugin for CudaText.
automatically saves modified files. currently: only named tabs (ignores untitled tabs).
it has config file with few options, call it by menu "Options / Settings-plugins / Auto Save".

options:
- "save_interval" (number, default: 30)
  interval of timer which auto-saves files, in seconds. 
  to disable auto-saving by timer, set to 0.

- "save_before_closing_tab" (0 or 1, default: 0)
  enables to auto-save file just before its closing (without any confirmation).

- "on_deactivate" (0 or 1, default: 0)
  enables to auto-save when CudaText looses focus.
  requires CudaText 1.114+.

author: Alexey Torgashin (CudaText)
license: MIT

```</details>----------
   
   
Name: AutoIt Helper  
Description: Autocompletion and function hints for AutoIt Lexer  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives IntelliSense commands for AutoIt lexer.

1) Auto-completion (Ctrl+Space)
   Place caret after incomplete function/class/variable name, and press this hotkey.
2) Go to definition
   Place caret on name of func/class/variable/const, and call "Go to definition" menu item from editor context menu.
3) Show function call-tip (Ctrl+Shift+Space)
   Place caret after function name between () brackets, and press this hotkey.
4) Auto-insert args for function (Tab)
   Place caret after function name and press this hotkey. Or press this hotkey after Auto-completion.
5) Show function doc-string
   Shows doc-string for function/class under caret, in the Output panel. Call it from Commands dialog or from Plugins menu.

Plugin uses local copy of 'au3.api' file. You can download latest version this file from:
    https://www.autoitscript.com/autoit3/scite/download/au3.api
    
Plugin needs to know path to AutoIt installation, so you must call menu item in "Option / Settings-plugins / AutoIt Helper" to specify this path. Otherwise, IntelliSense doesn't work and gives error in Console panel.

Authors: OlehL, Tom Braider.
License: MIT

```</details>----------
   
   
Name: Backup File  
Description: Creates backup copy of current file, a) by command in Plugins, b) auto-creation before file saving  
<details><summary>readme</summary>
```
Plugin for CudaText.
Creates backup copy of current file: a) by command in Plugins, b) by auto-creation on file saving.

Also gives command to call file-compare: current text, and previous backup copy.
For compare, it calls diff (Unix) or WinMerge (Windows).

Filename of copy - customizable via templates. Templates have macros for year/month/day/hours/etc, and
macros for parts of filename. See the help text, by pressing Help button in Config dialog.
Has macros for number counter, for upper/lower case. 


Author: Andrey Kvichanskiy (kvichans, at forum/github)
License: MIT

```</details>----------
   
   
Name: Calc Expression  
Description: Gets selected math expression, e.g. "2.4 * sin(pi/3)", calculates it, replaces selection with result  
<details><summary>readme</summary>
```
plugin for CudaText.
reads selected text as math expression, e.g. "2.4*sin(pi/3)" and evaluates it by Python.
tries to use "safe evaluation", without dangerous python functions enabled.
gives commands (menu Plugins / Calc Expression) to replace selection with number result,
or just show the result in the statusbar.

these Python functions are supported:

  abs      cosh       frexp      pow
  acos     degrees    hypot      radians
  asin     e          ldexp      sin
  atan     exp        log        sinh
  atan2    fabs       log10      sqrt
  ceil     floor      modf       tan
  cos      fmod       pi         tanh

  min(x1, x2, ...)
  max(x1, x2, ...)
  sum( [x1, x2, ...] )
  mean( [x1, x2, ...] )
  median( [x1, x2, ...] )

details:
https://docs.python.org/3/library/math.html
https://docs.python.org/3/library/statistics.html

plugin has config file, call menu item "Options / Settings-plugins / Calc Expression / Config".
it has separator options:
  [calc_expression]
  decimal_separator=.
  thousand_separator=
  list_separator=,
  digits_precision=4

decimal_separator can be changed to e.g. "," or another.
thousand_separator can be set to non-empty, it will be skipped by Python anyway.
list_separator is used in functions with several arguments, e.g. min, max, mean.
digits_precision is number of digits after decimal separator, can be 0 to show as is.


author: Alexey Torgashin (CudaText)
license: MIT

```</details>----------
   
   
Name: Caret History  
Description: Tracks caret pos changing (only long jumps), and allows to jump backward/forward by that history  
<details><summary>readme</summary>
```
Plugin for CudaText.
Plugin tracks changes of caret position, and when caret jumps long (more than 10 lines, option), it adds history point. So plugin keeps history of long caret jumps. It gives 2 commands: move backward, move forward, they change caret using this history. Short caret movements don't add to history (but they correct current history item). History length is 5 items by default (option).

The following scenario is working: you open file, jump to the end of file, history point is added, then "move backward" moves to begin of file. Then short editings don't change history, and "move forward" jumps to file end. Then short editings don't change history, and "move backward" jumps to file begin.

Author of idea: 
	github.com/eastorwest
Author: 
	Andrey Kvichanskiy (kvichans, at forum)

```</details>----------
   
   
Name: Case Converter  
Description: Converts identifiers between several cases (snake_case, camelCase, PascalCase etc)  
<details><summary>readme</summary>
```
Plugin for CudaText.
It allows to change case of current word, or words at several carets, between variants:

the_snake_case
THE_UPPER_CASE
theCamelCase
ThePascalCase 

Author: Alexey Torgashin
License: MIT

```</details>----------
   
   
Name: Color Picker  
Description: Shows color-picker dialog, inserts color #rrggbb  
<details><summary>readme</summary>
```
plugin for CudaText.
gives commands in "Plugins" menu.

1) show Color Picker dialog.
dialog is native for OS.

if caret is placed on HTML color token, e.g. #f0a020 or #ab0, dialog must show this color first.
on closing Color Picker with OK, plugin inserts chosen color (in form #rrggbb) into text.

2) command to show listbox with recently chosen colors.
this list is saved to settings/plugins.ini (up to 30 items).


author: Alexey Torgashin (CudaText)
license: MIT

```</details>----------
   
   
Name: Color Text  
Description: Allows to colorize text fragments, like function "Style token" in Notepad++  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives commands to colorize text fragments with several styles
(background color + font style: italic/bold/strikeout).
It is like function "Style token" in Notepad++.
Uses selected text, without selection uses word under first caret.

Gives menu item in "Options/ Settings-plugins" to edit config file.
Options:
- all_words: Colorize all occurrences of fragment
- case_sensitive: Case sensitive search for other occurrences
- whole_words: Colorize only those occurrences, which are whole words
- show_on_map: Show added colored marks also on micro-map.

Plugin also saves applied attribs to helper file (*.cuda-colortext) and 
restores attribs later on file opening. On applying attrib, plugin marks 
file as "modified", it is Ok, it's needed to save helper file.


Authors:
  Alexey T.
  Khomutov Roman
License: MIT

```</details>----------
   
   
Name: Colored Indent  
Description: Colorizes spaces/tabs in indents  
<details><summary>readme</summary>
```
plugin for CudaText.
gives highlighting of indentation levels. by default, highlights only 4 indentation 
levels in different background colors, next levels are colored in loop.

detects indentation level from editor setting "tab_size".
if some indentation is incorrect (e.g. 5-7 chars with "tab_size":4), then 
it's highlighted in special color.

plugin has config file, to open it: "Options / Settings-plugins / Colored Indent / Config".
- "lexers": ","-separated lexers, for which plugin is active.
- "color_set": ","-separated list of syntax-theme elements, from which background colors are taken.
- "color_error": syntax-theme element, from which error color is taken.
- "max_lines": maximal count of lines in document, when plugin is active.
- "active": persists activation state of plugin to restore it in next session.

plugin adds a menu entry to manually reload its config file: "Plugins / Colored Indent / Reload config".

plugin works on events: after file opened; after text is changed and short pause is passed.

author: Alexey Torgashin (CudaText)
enhancements: Andreas Heim (dinkumoil)
license: MIT

```</details>----------
   
   
Name: Column Marks  
Description: Commands to work with additional margins (options "margin", "margin_string")  
<details><summary>readme</summary>
```
plugin for CudaText.
gives commands to work with vertical lines, "margins".
CudaText has 2 options:
- margin
- margin_string (numbers space-separated)

plugin reads all these margins, and gives commands:

- Set fixed margin: prompts for value of fixed margin (no need to change config).
- Set additional margins: prompts for additional margins (no need to change config).
  Can enter empty string to remove additional margins.
- Jump left: puts caret (needs single caret) on the lefter margin (or column 0).
- Jump right: puts caret on the righter margin.

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: Complete From Text  
Description: Handles auto-completion command (Ctrl+Space) and gives list of words from the current document (or all documents, by option), starting from the currently typed word.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Handles auto-completion command (default hotkey: Ctrl+Space).
Gives completion listbox with words from current document, starting with the current word (under caret).
E.g. if you typed "op", it may show words "operations", "opinion", "option" etc.
Plugin cannot work with multi-carets. 

Plugin has options in the config file, call menu item "Options / Settings-pligins / Complete From Text".
Options are: 

- 'lexers': comma-separated lexer names, ie for which lexers to work; specify none-lexer as '-'.
- 'min_len': minimal word length, words of smaller length will be ignored.
- 'max_lines': if document has bigger count of lines, ignore this document.    
- 'case_sens': case-sensitive; words starting with 'A' will be ignored when you typed 'a'.
- 'no_comments': ignore words inside "syntax comments" (lexer specific).
- 'no_strings': ignore words inside "syntax strings" (lexer specific).
- 'what_editors': which documents (ie UI tabs) to read to get words. Values:
    0: only current document.
    1: all opened documents.
    2: all opened documents with the same lexer.

Plugin supports CudaText option "nonword_chars", so for example char '$' can be founds in words too,
if option is configured so.


Author: Alexey Torgashin (CudaText)
License: MIT

```</details>----------
   
   
Name: Config Toolbar  
Description: Configures main toolbar in CudaText: icon-set and buttons  
<details><summary>readme</summary>
```
Plugin for CudaText.
Allows to configure main toolbar (on the top):
- hide some standard buttons (specify 0-based button indexes, e.g. "0 2 8 9")
- add additional buttons.

For additional buttons you can customize: 
- caption 
- tooltip 
- icon file (size can be any, can mismatch current icon set) 
- command: usual CudaText commands + plugin commands, you can choose both in menu (like CudaText Commands dialog).

Notes:
- buttons can have caption, or icon, or caption+icon.
- dialog field "Visible for lexers" needs comma-separated lexer names, in any case. None-lexer must be specified as "-" char. Empty field: button is always visible.
- buttons cannot be changed during configuring time, they will be changed after CudaText restart.

Author: Alexey Torgashin (CudaText)
License: MIT

```</details>----------
   
   
Name: Configure Hotkeys  
Description: Shows dialog to view/set hotkeys in editor  
<details><summary>readme</summary>
```
Plugin for CudaText.
Manager for setting, removing, reporting of hotkeys

Author: Andrey Kvichanskiy (kvichans, at forum/github)
```</details>----------
   
   
Name: Config Menu  
Description: Allows to customize CudaText top/context menus, using JSON files  
<details><summary>readme</summary>
```
Plugin for CudaText.
Configures menus, top and context menu (on app start). 
Default config file:
	settings\menu.json
Other file can be set by option in user.json:
	"config_menus_from"

Author: Andrey Kvichanskiy (kvichans, at forum)


==========
What parts of menus can be configured?
==========

    Can change items of main menu (File, Edit, ...).
    Can change items of File except submenu "Open recent".
    Can change items of Edit, Selection, Search, View, Options, Help.
    Can change items of context menu for editor text.
    Not changeable items in other context menus (for gutter, for tab header...)

Can-change means that you can rename/remove/move all native items and can add any others. 
Indeed you can first clear all native items and then add needed ones. Or keep native items and add needed to the end.

Filling menus is like creating a tree, you can not only add items, but add submenus of any level.
Note that some submenus are autofilled:
    "recents" - recent-files submenu (natively in File)
    "themes" - Color-themes submenu (natively in Options)
    "plugins" - Plugins submenu (natively as item of main menu)

Needed commands you can find in two collections:
    Native commands (see names in file py\cudatext_cmd.py, which start with cmd_ or cCommand_)
    All plugins commands (see install.inf files for all installed plugins, or items in settings\plugins.json)

==========
Settings
==========
After plugin installation (and restart of app) file menu.json appears in directory settings. 
It allows to repeat (not all but most) native menus and it is good to start experiments.

Settings for plugin in user.json:
    Option "config_menus_from" - config file name (e.g. "menu.json") which will be read from dir settings.
    Option "config_menus_on_start" - values true/false - to apply config file when app starts.
    Option "config_menus_on_focus" - values true/false - to apply config file when text editor gets focus. 
		Only true-value here allows to use adaptive menus (menus for current lexer).

Better to rename file menu.json to my-menu.json and to write option "config_menus_from" in user.json. 
Original menu.json can be updated in the future with plugin update.

Note that option "config_menus_from" can have different values for different lexers. 
Thus you can use lexer-specific menus. 
For this you can open current lexer settings (Options/ Settings - more/ Settings - lexer overide) and set value for option "config_menus_from".

Example:
    In settings/user.json
        "config_menus_from":"my-menu.json" (sets all my menus)
    In settings/lexer Python.json
        "config_menus_from":"menu Python.json" (changes for menus to work with Python)
    In settings/lexer JSON.json
        "config_menus_from":"menu JSON.json" (changes for menus to work with JSON)

==========
JSON file format
==========
Brief view of file content:
{
  "top-file":{"how":"clear", ...all new items for native File menu...},
  "top-help":{"how":"add", ...additional items for native Help menu...},
}

Notes
    Root keys (like "top-file" and "top-help" above) must be only from the list
        "top",
        "top-file",
        "top-edit",
        "top-sel",
        "top-sr",
        "top-view",
        "top-op",
        "top-help",
        "text"
    You can use any subset of the list. 
    Lexer-menus can rebuild only context menu ("text").
    Root key "top" is to rebuild main menu. You can use other menuitem names (eg "Find" instead of "Search"), change order, skip something (e.g. Help) or add new items.
    Root key "text" is to rebuild context (local) menu for editor text.
    Pair "how":"clear" is to clear all items. It is default.
    Pair "how":"add" is to add items at end.

Brief view of one branch:
  "top-file":{
    sub:[
      {"cap":"Save file", "cmd":"cmd_FileSave"},
      {"cap":"Lines", 
       "sub":[
         {"cap":"Trim all", "cmd":"cCommand_TextTrimSpacesAll"},
         {"cap":"-"},
         {"cap":"My Split","cmd":"my_plug,split"},
       ],
      },
    ],
  },

Notes
    Value for key "cap" is caption for item or submenu.
    Pair "cap":"-" means menu separator.
    Values for key "cmd" are
        names from py\cudatext_cmd.py (starting with cmd_ or cCommand_),
        strings "module,method" for any plugin module and method in it.

```</details>----------
   
   
Name: Configure PyCodeStyle linter  
Description: Shows dialog to configure PyCodeStyle linter, and save its config  
<details><summary>readme</summary>
```
Plugin for CudaText.
It is helper for "Linter for Python using PEP8". It configurates PEP8 with dialog, and saves config file. File path is:

- Windows: c:\Users\name_here\.pep8
- Unixes: ~/.config/pep8 
  (if env var XDG_CONFIG_HOME is found, it is used instead of ~/.config)

Author: Andrey Kvichanskiy (kvichans, at forum/github)

```</details>----------
   
   
Name: CSS CanIUse  
Description: For CSS files, shows info about selected word from CanIUse.com site  
<details><summary>readme</summary>
```
Plugin for CudaText.
Adds menu item "Plugins / CSS CanIUse". For CSS based lexers (CSS, SCSS, LESS, Sass, Stylus) 
it opens http://caniuse.com with info about selected text (or current word if none is selected).

Author: Alexey T. (CudaText)
License: MIT

```</details>----------
   
   
Name: CSS Inspector  
Description: Plugin shows in HTML document CSS properties of current tag  
<details><summary>readme</summary>
```
CSS Inspector Plugin for CudaText.
In HTML documents it shows CSS properties of current tag under caret.
To call plugin, use menu item "Plugins / CSS Inspector", it will show side panel, and later you can switch to this panel (e.g. after calling Code Tree) by sidebar button with icon "css".

Properties given by: class; id; "style" tag.
Properties can be set:
  - straight in HTML by using "style" tag
  - in the CSS file and connected by the "link" tag

Libraries
---------
- Windows: plugin uses local libraries in its folder.
- Unix: plugin needs additional libs in OS Python, install them like this:
$ pip3 install lxml
$ pip3 install cssselect

Authors:
  @Medvosa at GitHub
  Alexey Torgashin (CudaText)
License: MIT

```</details>----------
   
   
Name: CSS Property Info  
Description: Shows information about selected CSS property in statusbar  
<details><summary>readme</summary>
```
plugin for CudaText.
works for CSS lexers: CSS, SCSS, Sass, LESS, Stylus and HTML.
uses database of site htmlbook.ru.

when single-line selection is made, plugin finds such CSS property in its database and shows information about that property in the statusbar. for example, if property is [IE 9.0+, Chrome 19.0+/26.0+, Firefox 16.0+, etc], plugin shows: "IE 9; Chr 19/26; Mz 16".

IE: Internet Explorer
Chr: Chrome
Op: Opera
Sf: Safari
Mz: Firefox
An: Android
iOS: iOS

config file is available, use menu item: Options / Settings-plugins / CSS Property Info / Config.
option "status_alt": if "1", then result will be shown in the alternative (yellowish) statusbar.

author: Medvosa, https://github.com/medvosa
license: MIT

```</details>----------
   
   
Name: CSS Table of Contents  
Description: For CSS files: creates table-of-contents, its sections/sub-sections  
<details><summary>readme</summary>
```
plugin for CudaText.
works for CSS lexers: CSS, SCSS, Sass, LESS, Stylus and HTML.
uses database of site htmlbook.ru.

when single-line selection is made, plugin finds such CSS property in its database and shows information about that property in the statusbar. for example, if property is [IE 9.0+, Chrome 19.0+/26.0+, Firefox 16.0+, etc], plugin shows: "IE 9; Chr 19/26; Mz 16".

IE: Internet Explorer
Chr: Chrome
Op: Opera
Sf: Safari
Mz: Firefox
An: Android
iOS: iOS

config file is available, use menu item: Options / Settings-plugins / CSS Property Info / Config.
option "status_alt": if "1", then result will be shown in the alternative (yellowish) statusbar.

author: Medvosa, https://github.com/medvosa
license: MIT

```</details>----------
   
   
Name: CSV Helper  
Description: Highlights columns in CSV and TSV files with different colors. Gives several commands to manage columns. Requires "CSV" and "TSV" lite lexers installed.  
<details><summary>readme</summary>
```
Plugin for CudaText.
For CSV (comma-separated values) and TSV (tab-separated values), plugin highlights
different columns in different colors.
Requires "CSV" and "TSV" pseudo lexers (plugin has these lexers as requirements
in Addon Manager, so they are usually auto-intalled).

Also plugin handles hovering mouse over text: it shows index/caption of current
column in the statubar (caption is read from the first line).

Plugin has several commands for manage columns.

Plugin has several options in config file. Call config by menu "Options / Settings-plugins / CSV Helper".

After changing config file perform a reload of opened CSV and TSV files in order
to apply new settings.

Authors:
  Alexey Torgashin (CudaText)
  Artem Gavrilov https://github.com/Artem3213212
  Oleh Lutsak https://github.com/OlehL
License: MIT

```</details>----------
   
   
Name: CSV Helper  
Description: Highlights columns in CSV and TSV files with different colors. Gives several commands to manage columns. Requires "CSV" and "TSV" lite lexers installed.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Additional commands for CudaText in Commands dialog and Plugins menu

Menu items

- Find/Replace
	- Find clipbrd: next
	- Find clipbrd: previous
	- Replace all occurrences of selected string with clipbrd
	-
	- Copy word or [string] or 'string' (no selection)
	- Replace word or [string] or 'string' with clipbrd (no selection)
	- Expand selection to word or "string" or (string)
	- Expand and Copy selection to word or "string" or (string)
	-
	- Remove all ASCII chars 0..31 (excluding 9,10,13)
- Insert
	- Add indented line above
	- Add indented line below
	-
	- Paste to first column
	- Paste with indent above
	- Paste with indent below
	- Paste like Lazarus IDE
	-
	- Fill selection by string...
	- Insert unicode char
- Jump
	- To matching bracket
	-
	- To next changed lines
	- To previous changed lines
	- To next saved lines
	- To previous saved lines
	- To next working lines
	- To previous working lines
	-
	- To line with number in clipbrd
	-
	- Left into CamelCase/snake_case
	- Right into CamelCase/snake_case
	- Left into CamelCase/snake_case and select
	- Right into CamelCase/snake_case and select
	-
	- Bookmark list for current tab
	- Bookmark list for all tabs
	- Numbered bookmark list for all tabs
- Scroll
	- Current line to screen center
	- Current line to screen top
	- Current line to screen bottom
	-
	- Screen to left
	- Screen to right
-Navigate
	- Open file by selected name
	-
	- Open file(s) in nearest right tab(s)...
	- Open file(s) in nearest left tab(s)...
	-
	- Navigate by error in console
-Tabs
	- Activate previously active tab (go back)
	-
	- Move tab to position...
	-
	- Activate tab #1 in group #1
	- Activate tab #2 in group #1
	- Activate tab #3 in group #1
	- Activate tab #4 in group #1
	- Activate tab #5 in group #1
	- Activate tab #6 in group #1
	- Activate tab #7 in group #1
	- Activate tab #8 in group #1
	- Activate tab #9 in group #1
	- Activate tab #1 in group #2
	- Activate tab #2 in group #2
	- Activate tab #3 in group #2
	- Activate tab #4 in group #2
	- Activate tab #5 in group #2
	- Activate tab #6 in group #2
	- Activate tab #7 in group #2
	- Activate tab #8 in group #2
	- Activate tab #9 in group #2
	- Activate last tab in group #1
	- Activate last tab in group #2
	- Activate next tab (global loop)
	- Activate previous tab (global loop)
	-
	- Other group
		- Close active tab in next group
		- Close active tab in previous group
		-
		- Switch tab to next in next group
		- Switch tab to next in previous group
		- Switch tab to previous in next group
		- Switch tab to previous in previous group
		-
		- Switch tab to first in next group
		- Switch tab to first in previous group
		- Switch tab to last in next group
		- Switch tab to last in previous group
- Splitters
	- Expand side panel
	- Narrow side panel
	-
	- Expand bottom panel
	- Narrow bottom panel
	-
	- Expand top-left group
	- Narrow top-left group
	-
	- Expand active group
	- Narrow active group
- Paragraph
	- Go to beginning
	- Go to end
	- Go to next
	- Go to previous
	-
	- Align: Configure...
	- Align: Left justify 
	- Align: Right justify 
	- Align: Center justify 
	- Align: Fully justify 
- Code Tree
	- Show current path in statusbar
	- Set active node, nearest to caret
- Align
	- Reindent selected lines...
	- Indent lines like the first selected
	- Align in lines by separator...
	-
	- Join selected lines
	- Delete duplicate spaces
	-
	- Re-wrap/split lines by margin
	- Re-wrap/split comment at caret
	- Align in lines to center by margin
	- Align in lines to right by margin
- File
	- Open recent file...
	-
	- Rename file...
	- New file and save in current folder...
	- Open all files from folder with sub-folders...
	- Open current file in default application

Author: Andrey Kvichanskiy (kvichans, at forum/github)
License: MIT

```</details>----------
   
   
Name: CSV Helper  
Description: Highlights columns in CSV and TSV files with different colors. Gives several commands to manage columns. Requires "CSV" and "TSV" lite lexers installed.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Additional commands for CudaText in Commands dialog and Plugins menu

Menu items

- Find/Replace
	- Find clipbrd: next
	- Find clipbrd: previous
	- Replace all occurrences of selected string with clipbrd
	-
	- Copy word or [string] or 'string' (no selection)
	- Replace word or [string] or 'string' with clipbrd (no selection)
	- Expand selection to word or "string" or (string)
	- Expand and Copy selection to word or "string" or (string)
	-
	- Remove all ASCII chars 0..31 (excluding 9,10,13)
- Insert
	- Add indented line above
	- Add indented line below
	-
	- Paste to first column
	- Paste with indent above
	- Paste with indent below
	- Paste like Lazarus IDE
	-
	- Fill selection by string...
	- Insert unicode char
- Jump
	- To matching bracket
	-
	- To next changed lines
	- To previous changed lines
	- To next saved lines
	- To previous saved lines
	- To next working lines
	- To previous working lines
	-
	- To line with number in clipbrd
	-
	- Left into CamelCase/snake_case
	- Right into CamelCase/snake_case
	- Left into CamelCase/snake_case and select
	- Right into CamelCase/snake_case and select
	-
	- Bookmark list for current tab
	- Bookmark list for all tabs
	- Numbered bookmark list for all tabs
- Scroll
	- Current line to screen center
	- Current line to screen top
	- Current line to screen bottom
	-
	- Screen to left
	- Screen to right
-Navigate
	- Open file by selected name
	-
	- Open file(s) in nearest right tab(s)...
	- Open file(s) in nearest left tab(s)...
	-
	- Navigate by error in console
-Tabs
	- Activate previously active tab (go back)
	-
	- Move tab to position...
	-
	- Activate tab #1 in group #1
	- Activate tab #2 in group #1
	- Activate tab #3 in group #1
	- Activate tab #4 in group #1
	- Activate tab #5 in group #1
	- Activate tab #6 in group #1
	- Activate tab #7 in group #1
	- Activate tab #8 in group #1
	- Activate tab #9 in group #1
	- Activate tab #1 in group #2
	- Activate tab #2 in group #2
	- Activate tab #3 in group #2
	- Activate tab #4 in group #2
	- Activate tab #5 in group #2
	- Activate tab #6 in group #2
	- Activate tab #7 in group #2
	- Activate tab #8 in group #2
	- Activate tab #9 in group #2
	- Activate last tab in group #1
	- Activate last tab in group #2
	- Activate next tab (global loop)
	- Activate previous tab (global loop)
	-
	- Other group
		- Close active tab in next group
		- Close active tab in previous group
		-
		- Switch tab to next in next group
		- Switch tab to next in previous group
		- Switch tab to previous in next group
		- Switch tab to previous in previous group
		-
		- Switch tab to first in next group
		- Switch tab to first in previous group
		- Switch tab to last in next group
		- Switch tab to last in previous group
- Splitters
	- Expand side panel
	- Narrow side panel
	-
	- Expand bottom panel
	- Narrow bottom panel
	-
	- Expand top-left group
	- Narrow top-left group
	-
	- Expand active group
	- Narrow active group
- Paragraph
	- Go to beginning
	- Go to end
	- Go to next
	- Go to previous
	-
	- Align: Configure...
	- Align: Left justify 
	- Align: Right justify 
	- Align: Center justify 
	- Align: Fully justify 
- Code Tree
	- Show current path in statusbar
	- Set active node, nearest to caret
- Align
	- Reindent selected lines...
	- Indent lines like the first selected
	- Align in lines by separator...
	-
	- Join selected lines
	- Delete duplicate spaces
	-
	- Re-wrap/split lines by margin
	- Re-wrap/split comment at caret
	- Align in lines to center by margin
	- Align in lines to right by margin
- File
	- Open recent file...
	-
	- Rename file...
	- New file and save in current folder...
	- Open all files from folder with sub-folders...
	- Open current file in default application

Author: Andrey Kvichanskiy (kvichans, at forum/github)
License: MIT

```</details>----------
   
   
Name: CudaFormatter  
Description: Framework to use code formatters as 2nd-level plugins  
<details><summary>readme</summary>
```
Framework to use code formatters in CudaText. Formatters are Python functions which change entire file text or only selected text. Formatters are distributed as separate 2nd-level plugins, which are called via this framework. This approach is like CudaLint and its linters.

Commands in Plugins menu
------------------------

- Formatter (menu): Runs formatter for current editor file. If several formatters are found, menu dialog will suggest to choose one of them.

- Formatter A...D: Runs formatter for current editor file, which has label (A, B, C, D) set. Labels are configurable by another command.

- Configure on_save: Chooses which formatters are active on file saving. The first formatter, which is suitable for current lexer, and has the flag "on_save", will be used to format text on file saving.

- Configure labels: Allows to assign labels (A, B, C, D) to formatters. Labels allow to use commands "Formatter A"..."Formatter D", e.g. via hotkeys. So you can use command "Formatter A" via some hotkey, and be sure that for all lexers "Formatter A" will use desired formatters.

- Configure formatter: For those formatters which support config file, command will suggest to open global config file (in the folder "settings" of CudaText).

- Configure formatter (local): For those formatters which suppots config file, command will suggest to open "local" config (in the folder of current editor file). If local config not exists, plugin will suggest to create it from global config.

Docs
----
No docs yet.
To see how to write formatters, install "Formatters for JavaScript" which has most of features.


Author: Alexey Torgashin (CudaText)
License: MIT

```</details>----------
   
   
Name: Kvichans lib to use in any plugins  
Description: Utilities for logging, i18n, storing plugin options/states and so on  
<details><summary>readme</summary>
```
﻿Library for logging, i18n, storing plugin options/states and so on.

Author: Andrey Kvichansky    (kvichans on github.com)
License: MIT

Library contents:

============
1. log
Function to show variables logging, with timestamps and caller info.

- It has built-in str.format - so such 2 calls are identical:
    log(s, args, kwargs)
    log(s.format(args, kwargs))
- Automatic duration time calculation
- Automatic detection of caller info

Examples:
Simple call
    log('a={}', 1)
    Prints to sys.stdout this string:
    [12.34"]fn:123 a=1
    Where:
    [12.34"]        Total elapsed time, from the moment of logging start.
    fn              Name of module/function/method caller.
    123             Index of line, where log is called.

Other features
    log('###')      Prints additional line with call stack.
                    ### fn:123 fn2:354 <module>:89
    log('¬¶')       Automatic replacement of "¬" to chr(9), "¶" to chr(10).

Redirection of output
    To output logging to file dir/my.log, do this:
        Tr.tr=Tr('dir/my.log')
    To return logging back to sys.stdout, do this:
        Tr.tr=Tr()

============
2. (i18n) get_translation
Utility to substitute strings via current CudaText translation.
How to use:
    In your module do assignment
        _   = get_translation(__file__)
    In places, where you want to translate strings, do this
        msg(_('my text'))

After that, collection of all such constants, and their translation, are possible via
- Standard Python utility pygettext
- Application like Poedit
Switching of translations is performed in sync with CudaText.

============
3. Saving/loading of data to/from JSON format.
Purpose is to give plugins the utility to store their settings.
Saving
    def set_hist(key_or_path,
                 value=None,
                 module_name='_auto_detect',
                 kill=False,
                 to_file=PLING_HISTORY_JSON)
Loading
    def get_hist(key_or_path,
                 default=None,
                 module_name='_auto_detect',
                 to_file=PLING_HISTORY_JSON)

- Location of file.
File name is given by parameter to_file.
If it's missed, then used "settings/plugin history.json".
If value of to_file is not the full path, then the path of "settings" folder is used.

- Sharing of settings.
For different plugins to be able to store their settings in a single file,
use parameter "module_name". If it's not set, then JSON file will have a branch with the
module name, from which set_hist/get_hist were called. Or you can set this branch by parameter.
If module_name=None, then branch will not be created, and all data will go to JSON root.
This may be handy, when plugin uses its own file.

- Location in file.
Parameter key_or_path specifies the key in JSON file, which will be stored/loaded.
It can be string - then it's location of the key (it can be inside module_name branch).
It can be list of string - then it's list of nested nodes of JSON tree.
On saving, all nodes are created automatically.
    But if existing JSON node is specified as intermediate node, library gives KeyError.

- Deletion of keys/branches.
If in set_hist you set kill=True, and key/branch specified by "key_or_path", exists,
then it will be deleted. In this case, parameter "value" is ignored.

- Comments and custom formatting (indents and spaces) are not kept on saving.
They are kept only in user.json, on saving via set_opt.

- Return.
In loading, if any of intermediate keys missed, or the final key is missed, you'll get default.
In saving, you'll get:
- parameter "value" value, if it's successfully saved.
- value previously stored by "key_or_path", if you used kill=True, and deletion performed.
- None, if you used kill=True, but key was not found.

============
4. Misc
- Short names
odict       = collections.OrderedDict
T,F,N       = True, False, None
c13,c10,c9  = chr(13),chr(10),chr(9)

- Short call of str.format
Instead of
    msg('a {}, b {}'.format('A', 'B'))
you can use
    msg(f('a {}, b {}', 'A', 'B'))

- Command to run current Python file, like it's CudaText plugin:
    "Execute current file as plugin"
Saves current file.
Clears console output.
Runs the file.

```</details>----------
   
   
Name: Kvichans lib to use in any plugins  
Description: Utilities for logging, i18n, storing plugin options/states and so on (Python 3.5)  
<details><summary>readme</summary>
```
﻿Library for logging, i18n, storing plugin options/states and so on.

Author: Andrey Kvichansky    (kvichans on github.com)
License: MIT

Library contents:

============
1. log
Function to show variables logging, with timestamps and caller info.

- It has built-in str.format - so such 2 calls are identical:
    log(s, args, kwargs)
    log(s.format(args, kwargs))
- Automatic duration time calculation
- Automatic detection of caller info

Examples:
Simple call
    log('a={}', 1)
    Prints to sys.stdout this string:
    [12.34"]fn:123 a=1
    Where:
    [12.34"]        Total elapsed time, from the moment of logging start.
    fn              Name of module/function/method caller.
    123             Index of line, where log is called.

Other features
    log('###')      Prints additional line with call stack.
                    ### fn:123 fn2:354 <module>:89
    log('¬¶')       Automatic replacement of "¬" to chr(9), "¶" to chr(10).

Redirection of output
    To output logging to file dir/my.log, do this:
        Tr.tr=Tr('dir/my.log')
    To return logging back to sys.stdout, do this:
        Tr.tr=Tr()

============
2. (i18n) get_translation
Utility to substitute strings via current CudaText translation.
How to use:
    In your module do assignment
        _   = get_translation(__file__)
    In places, where you want to translate strings, do this
        msg(_('my text'))

After that, collection of all such constants, and their translation, are possible via
- Standard Python utility pygettext
- Application like Poedit
Switching of translations is performed in sync with CudaText.

============
3. Saving/loading of data to/from JSON format.
Purpose is to give plugins the utility to store their settings.
Saving
    def set_hist(key_or_path,
                 value=None,
                 module_name='_auto_detect',
                 kill=False,
                 to_file=PLING_HISTORY_JSON)
Loading
    def get_hist(key_or_path,
                 default=None,
                 module_name='_auto_detect',
                 to_file=PLING_HISTORY_JSON)

- Location of file.
File name is given by parameter to_file.
If it's missed, then used "settings/plugin history.json".
If value of to_file is not the full path, then the path of "settings" folder is used.

- Sharing of settings.
For different plugins to be able to store their settings in a single file,
use parameter "module_name". If it's not set, then JSON file will have a branch with the
module name, from which set_hist/get_hist were called. Or you can set this branch by parameter.
If module_name=None, then branch will not be created, and all data will go to JSON root.
This may be handy, when plugin uses its own file.

- Location in file.
Parameter key_or_path specifies the key in JSON file, which will be stored/loaded.
It can be string - then it's location of the key (it can be inside module_name branch).
It can be list of string - then it's list of nested nodes of JSON tree.
On saving, all nodes are created automatically.
    But if existing JSON node is specified as intermediate node, library gives KeyError.

- Deletion of keys/branches.
If in set_hist you set kill=True, and key/branch specified by "key_or_path", exists,
then it will be deleted. In this case, parameter "value" is ignored.

- Comments and custom formatting (indents and spaces) are not kept on saving.
They are kept only in user.json, on saving via set_opt.

- Return.
In loading, if any of intermediate keys missed, or the final key is missed, you'll get default.
In saving, you'll get:
- parameter "value" value, if it's successfully saved.
- value previously stored by "key_or_path", if you used kill=True, and deletion performed.
- None, if you used kill=True, but key was not found.

============
4. Misc
- Short names
odict       = collections.OrderedDict
T,F,N       = True, False, None
c13,c10,c9  = chr(13),chr(10),chr(9)

- Short call of str.format
Instead of
    msg('a {}, b {}'.format('A', 'B'))
you can use
    msg(f('a {}, b {}', 'A', 'B'))

- Command to run current Python file, like it's CudaText plugin:
    "Execute current file as plugin"
Saves current file.
Clears console output.
Runs the file.

```</details>----------
   
   
Name: Kvichans lib with wrapper over dlg_proc and more dialog tools  
Description: Helper library to work with CudaText plugin dialogs  
<details><summary>readme</summary>
```
Helper library to work with CudaText plugin dialogs

Author: Andrey Kvichansky    (kvichans on github.com)
License: MIT

See github.com/kvichans/cuda_kv_dlg/wiki

```</details>----------
   
   
Name: Kvichans lib with wrapper over dlg_proc and more dialog tools  
Description: Helper library to work with CudaText plugin dialogs (Python 3.5)  
<details><summary>readme</summary>
```
Helper library to work with CudaText plugin dialogs

Author: Andrey Kvichansky    (kvichans on github.com)
License: MIT

See github.com/kvichans/cuda_kv_dlg/wiki

```</details>----------
   
   
Name: CudaLint  
Description: Linting (syntax-checking) of source code. Needs "linters" for each lexer you want to check. See useful help in readme folder.  
<details><summary>readme</summary>
```
CudaLint (plugin for CudaText).
It allows to check/validate syntax of current file, for many lexers. Each lexer must be supported
with additionally installed linter, for example:

- JavaScript is supported with linter based on JSLint tool,
- HTML is supported with linter based on HTML Tidy tool,
- CSS is supported with linter based on CSSLint tool,
- etc

You will find all linters in the Addon Manager: "Plugins / Addon Manager / Install".
Linters are installable like other plugins but they don't add commands, they only add folders
"[CudaText]/py/cuda_lint_*", which are automatically used by CudaLint.
After you install a linter, see readme in its folder, maybe how-to-use info is written there.

=== Node.js ===

Some linters require Node.js, so for those linters, you must install Node first.
Those linters are sometimes shipped with Node modules preinstalled (in plugin folder)
and sometimes you need to install Node modules via NPM.
See linter's readme file for details.

Windows: "node.exe" must be in PATH, command "node -v" must work in console.
Linux: "nodejs" package must be installed, command "nodejs -v" must work in terminal.

=== Usage ===

To run linting, use menu item "Plugins / CudaLint / Lint", or set hotkey to this command
(in CudaText Command Palette, press F9). You will see statusbar message, which tells how many errors
linter found. For each found error, you'll see yellow/red bookmark (you can use usual commands
for these bookmarks). Plugin also shows list of errors in the "Validate" panel
(to show Validate panel, click V icon on the CudaText sidebar).

Linting can be run by events:
- after opening file
- before saving file
- after text is changed + pause passed

Events aren't used by default (to not slowdown usual work). To use events, you must enable them in config.
Call config by menu item in "Options / Settings-plugins".

=== About ===

Authors:
- Alexey Torgashin (CudaText)
- TBeu, http://tbeu.de

CudaLint uses code portions from the SublimeLinter 3 project.
License: MIT

```</details>----------
   
   
Name: Dash Help  
Description: Opens Dash help pages, for selected text or current word  
<details><summary>readme</summary>
```
plugin for CudaText.
allows to call Dash help files (doc-sets) from CudaText. search is made from selected text, or current word if none is selected.

for macOS, you must install Dash app.
for Windows/Linux, install similar Zeal app, it uses Dash doc-sets too. https://zealdocs.org/

after installing, enable some doc-sets in Dash/Zeal options.
not all syntaxes have doc-sets, but main popular syntaxes do.

plugin gives commands for 2 main options:
- call help syntax-sensitive or not (ie, consider lexer name)
- run app in background or foreground


author: Alexey (CudaText)
license: MIT
used some code from Sublime Text plugin DashDoc.

```</details>----------
   
   
Name: Detect Indent  
Description: Detects indentation (spaces or tabs, tab size) for opened files  
<details><summary>readme</summary>
```
Plugin for CudaText
It handles on_open event, and detects indentation for opened file:
is it tabs/spaces, number of spaces.

Code is based on Sublime Text's plugin detect_indentation.py.
It is open source at https://github.com/randy3k/sublime-default

Adapted to CudaText by Alexey T.

```</details>----------
   
   
Name: DevDocs  
Description: Performs search on DevDocs site  
<details><summary>readme</summary>
```
This is command plugin for CudaText. 
It performs search with given words on DevDocs.io site.

Plugin has two commands: "Search by input", "Search by text". Command "Search by text" does search for current word at editor caret, or for current selected text if selection exists.

Examples:

    If you enter "js date", then search will be done for JavaScript "date" word;
    If you enter "html frame", then search will be done for HTML "frame" word;
    If you enter "php print", then search will be done for PHP "print" word (note: first enable PHP language on DevDocs site);
    If you enter one word, search for all languages (enabled on DevDocs site) will be done. 

Author: Alexey T.

```</details>----------
   
   
Name: Differ  
Description: Plugin to compare two files and show compare results side by side  
<details><summary>readme</summary>
```
Plugin for CudaText.
It compares two files and shows them side-by-side.
Plugin shows two files in a single tab.

It gives few commands in menu "Plugins / Differ".
Command "Refresh" runs comparision again, if one or both files were edited.
It has options dialog, call it via "Options / Settings-plugins / Differ / Config".


Authors:
  OlehL ( https://github.com/OlehL )
  Alexey Torgashin (CudaText)
  Andrey Kvichanskiy (kvichans on GitHub)
License: MIT

```</details>----------
   
   
Name: DocBlock  
Description: Helps to type DocBlock comments, for JS/PHP lexers  
<details><summary>readme</summary>
```
Plugin "DocBlock" for CudaText.
It helps to enter docblock comments for lexers: PHP, JavaScript, CoffeeScript.

  /**
   * Some text
   * here
   */

1) It handles Enter key press. Plugin looks, if end of current line is "/**", if so then empty docblock is entered and caret placed in it. If you type middle of docblock, ie begin of current line is indent + "* ", then plugin enters "* " on next line too.

2) Auto-completion works, for JavaScript and PHP: inside docblock type "@" and press Ctrl+Space (ie hotkey for auto-completion): you'll see list of JSDoc or PHPDoc tags. 


Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Draw Lines  
Description: Draws pseudo-graphic frames in text, by Shift+arrows  
<details><summary>readme</summary>
```
﻿plugin for CudaText.
allows to draw preudo-graphic frames in text, using Unicode "box" chars,
which were available in DOS codepage ages ago.

example of frames:
       ╒════╦═╗
       │   ╔╬═╬╤═╤═════╗
   ╒═╕ │   ╠╩╤╩╧═╧─┬─┐ ║
   └─┴─┤ ┌┬╨─┤    ┌┼─┼─╜
  ╙────┴─┴┴──┴────┴┴─┘

activate/deactivate plugin using menu item: Plugins - Draw Lines.
when active, plugin allows single/double line modes, toggle this by F9 
(no command in plugin, just a hotkey).
use Shift+arrows to draw line, single or double, in any of 4 directions:
up/down/left/right. line intersections are handled, so some chars will
be "crosses" or "angles" when you intersect other lines.

plugin subscribes to editor event only after call, so doesn't slow down
usual work.

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: EditorConfig Support  
Description: Supports EditorConfig system  
<details><summary>readme</summary>
```
plugin for CudaText.
supports EditorConfig system in editor. it reads/applies EditorConfig files 
for all opened files. supports the following options:

- "indent_style"; it sets CudaText option "tab_spaces" in memory
- "indent_size"; it sets CudaText options "tab_size" and "indent_size" in memory
- "tab_width"; it sets CudaText option "tab_size" in memory

beginning with CudaText 1.77.6:
- "end_of_line"; it changes line endings on file saving
- "charset"; it sets CudaText option "newdoc_encoding" but doesn't change current file encoding
- "trim_trailing_whitespace"; it's applied on file saving
- "insert_final_newline"; it's applied on file saving


author: Alexey Torgashin (CudaText)
license: MIT

```</details>----------
   
   
Name: Edits Navigation  
Description: Return to previously edited lines  
<details><summary>readme</summary>
```
Plugin for CudaText.
Adds a command to cycle through edited lines. 

To set hotkeys for commands, use F9 functionality in Command palette (Ctrl+Shift+P).
------------------------------

Commands in "Plugins / Edits Navigation" menu:

- "Go To Previous Edit"
   Cycle caret through previously edited lines

------------------------------

Authors:
  @halfbrained (at GitHub)

License: MIT

```</details>----------
   
   
Name: Emmet Lite  
Description: Emmet engine, see www.emmet.io  
<details><summary>readme</summary>
```
Emmet Lite plugin for CudaText.
See www.emmet.io for info.

Plugin gives 2 basic commands: "expand abbreviation", "wrap with abbreviation".
Uses Node.js, you must install it first.


Emmet profile can be changed using menu. Supported:
 - html    - default output profile. 
 - xhtml   - the same as "html", but outputs empty elements with closed slash: <br />. 
 - xml     - default for XML and XSL syntaxes: outputs each tag on a new line with indentation, empty elements are outputted with closing slash: <br/>. 
 - xml_zen - the same as "xml", but outputs leaf tags (i.e. tags without nested tags) with additional newline (e.g. <td> is leaf tag in table>tr>td). 
 - line    - used to output expanded abbreviation without any indentation and newlines. 
 - plain   - the same as "line", but doesn't move caret. 

Emmet syntax detected automatically:
- for lexers CSS/LESS/SCSS/SASS/Stylus it's "css"; 
- for lexers XML/XSLT it's "xsl"; 
- for others it's "html".

Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Encode  
Description: Allows to encode text using many transformations (Base64, URL escape, HTML/XML escape, Hash, etc)  
<details><summary>readme</summary>
```
Plugin for CudaText.
Allows to convert text (selected block or entire text if nothing selected) using many codings (transformations).
Ported from StringEncode: https://github.com/colinta/SublimeStringEncode
Later more codings were added.

Codings:

- HTML entitize: Converts characters to their HTML entity "&nnn;"
- HTML deentitize: Converts HTML entities to characters
- XML entitize: Converts characters to their XML entity
- XML deentitize: Converts XML entities to characters
- Safe HTML entitize: Converts characters to their HTML entity, but preserves HTML reserved characters
- Safe HTML deentitize: Converts HTML entities to characters, but preserves HTML reserved characters

- JSON escape: Escapes a string and surrounds it in quotes, according to the JSON encoding
- JSON unescape: Unescapes a string (including the quotes!) according to JSON encoding
- URL encode: Uses urllib.quote to escape special URL characters
- URL decode: Uses urllib.unquote to convert escaped URL characters

- Base64 encode/decode
- Base32 encode/decode
- Base16 encode/decode

- Quoted-printable: converts Unicode string to smth like =D0=9F=D1=80=D0=BE
- Unicode-escape: converts Unicode string to smth like \u041f\u0440\u043e

- MD5: Creates MD5 hash
- SHA256: Creates SHA256 hash
- SHA512: Creates SHA512 hash

- Escape regex: Escapes reg.ex. meta characters
- Escape LIKE: Escapes SQL-LIKE meta characters

- Decimal to Hex: converts decimal number to hex form (with 0x prefix)
- Hex to Decimal: converts hex number (0x prefix is optional) to decimal form

- Unicode Normalize (NFC, NFD, NFKC, NFKD): see description at https://en.wikipedia.org/wiki/Unicode_equivalence#Normal_forms 


Author: Alexey T (CudaText)
License: MIT

```</details>----------
   
   
Name: Explorer Integration  
Description: For Windows: allows to add/remove Explorer context menu item for CudaText, to associate CudaText with file-extensions .txt .ini .cuda-proj .cuda-session.  
<details><summary>readme</summary>
```
Plugin shows dialog to change options of Windows Explorer integration with CudaText. It is like SynWrite's dialog.
You can add/remove Explorer context menu item for CudaText. And associate Cuda with some file extensions: txt, ini, cuda-proj, cuda-session.

Author: Alexey T.
License: MIT

```</details>----------
   
   
Name: Extended Selection  
Description: Extend double/triple-click selection while holding Shift  
<details><summary>readme</summary>
```
A plugin to streamline the introduction of copy-paste bugs.
Adds to usual double-click selection:

    Shift+Double-click: includes additional characters to selection
    Shift+Triple-click: "expression selection" (useful for selecting function call with arguments)
    
-----------------------------

Plugin has options in the config file, call menu item
"Options / Settings-pligins / Extended Selection": 

Each lexer has following options:
"include_chars": additional characters to include in Shift+double-click selection. 
"stop_ext": characters to stop Shift+triple-click selection when not enclosed in ()[]{}<>
"open_chars" and "close_chars": map of opening-to-closing and closing-to-opening brackets. Used to limit selection extension to stay within brackets, and to ignore "stop_ext" characters inside brackets, when they follow selected text. 

For example when 'cc' clicked in following line:
	aa = bb.cc<dd>(ee=ff) = ww
	
* normal double-click will yield selection: 
	cc
* addon's shift+double-click: 
	bb.cc
	(period and adjacent text is added to selection because '.' is in the "include_chars" for this lexer)
* addon's shift+triple-click: 
	bb.cc<dd>(ee=ff)
	(selection stops at equal-signs at both sides because '=' is in the "stop_ext" for this lexer. "stop_ext" characters ('=' here) are ignored inside brackets)

-----------------------------

Commands in "Plugins / Extended Selection" menu:

- "Toggle Selection"
   Cycle through addon's double/triple-click selections.

-----------------------------
    
Author: Shovel (CudaText forum user)
License: MIT

```</details>----------
   
   
Name: ExtTools  
Description: Adds support for calling external programs in CudaText  
<details><summary>readme</summary>
```
Plugin for CudaText.
Allows to call external programs in CudaText.
Adds menu "Tools" (near "Plugins") with commands: 
    Config (customize tools),
    Run lexer main tool (analog of SublimeText's command "Build"), 
    Tool1...ToolN (items appear after tools are configured).

Config file is settings/exttools.json.

Details:
- "Shell command" option must be checked for tools which you want to run via OS-shell: 
  on Windows it's commands of cmd.exe. On Linux this opt usually not needed.
- If lexer(s) assigned to a tool, tool can be called only when these lexers active. 
- "Patterns" allow to parse output lines by regex, and find in these lines: 
  filename, line number, column number. If line parsed OK, you can jump to found
  line number and file by clicking in Output panel.


Author: A.Kvichanskiy (kvichans at forum/github)
License: MIT

```</details>----------
   
   
Name: Extract Strings  
Description: Shows dialog to enter RegEx, this RegEx will find list of strings. You can choose what to do with these strings: copy to clipboard, copy to new tab. Also includes Filter Lines command to find lines.  
<details><summary>readme</summary>
```
Plugin for CudaText.

Gives dialog "Extract Strings", like in SynWrite. This dialog can find, by regular expression, substrings in the current editor, and then a) Copy them to clipboard, b) Copy them to new tab.

Button "Reg.ex. for e-mail" sets regular expression to find e-mails.

Includes plugin "Filter Lines". Command to find (in current editor tab) all lines, which contain custom (entered in dialog) string, or reg.ex. Found lines are put to a new tab.

Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Favorites  
Description: Manages "favorites": list of user-selected file names, to quickly open them  
<details><summary>readme</summary>
```
Plugin for CudaText. Gives dialog to call favorite items.

- Files: click button "Add" in plugin dialog, to browse for a file.
- Folders: click button "Add" with Shift key, to choose a folder. Folders are shows with [] brackets in the dialog. Calling a folder item - suggests to open a file from that folder.
- Projects: use ui-tab "Projects" and press button "Add" to choose a project.

Non-existing items are marked by ? char in the list.

Dialog gives hotkeys to quickly call item by its index 1...9: 
- Alt+1, Alt+2, ..., Alt+9
- Ctrl+1, Ctrl+2, ..., Ctrl+9

Plugin can import favorites from SynWrite. To do it, browse for file "SynFav.ini", which is located in the Settings subfolder of SynWrite.


Author: Andrey Kvichanskiy (kvichans, at forum/GitHub)
License: MIT

```</details>----------
   
   
Name: File Type Profile  
Description: Create profiles for files with certain filename extensions and apply the settings automatically when opening a file.  
<details><summary>readme</summary>
```
================================================================================
File Type Profile plugin for CudaText
================================================================================

Create profiles for files with certain filename extensions and apply the
settings automatically when opening a file.

This plugin is especially useful when coding Windows Batch scripts or if you
have to write, for whatever reason, e.g. Linux shell scripts on a Windows
machine.


The Windows console still uses as character encoding schema the old DOS or OEM
code pages introduced back in the '80s by IBM. In nearly every country another
code page is used - and it's different from the default ANSI code page on the
same system.

If you write Batch scripts with an editor that uses the default ANSI code page
for your country, at its best your comments are displayed wrong when it comes to
other characters than the ones in the basic 7 bit ASCII range (character codes
from 32 to 127). But if you hard-code e.g. directory names into your script,
containing characters of your language with a character code beyond 127, you
will get a "Directory/File not found" error.

If you have to write Linux shell scripts on a Windows machine and forget to set
the end-of-line format to the Unix/Linux style you will produce a script file
which can not be executed.

These are the situations this plugin can help you.


================================================================================
Features
================================================================================

You can create profiles for certain file types (distinguished by their filename
extension, e.g. *.cmd, *.bat) and define the code page and/or the end-of-line
(EOL) format that should be set when a file matching a profile has been loaded.

When you want to start writing a script, AT FIRST create in Windows Explorer a
new file. Name it like you want and set its filename extension. Then open it in
CudaText. The plugin will automatically set the character encoding and/or the
EOL format according to your configuration.

The plugin doesn't change encoding or end-of-line format of a file if it is part
of a session or of the file history. That means you can override automatically
set encoding or EOL format and it will be restored at next time the file is
opened.

When CudaText runs the first time after plugin's installation, the plugin will
create a default config file in the CudatText settings directory. It contains
template profiles for Batch script and Linux shell script files but lacks the
value for Batch script's "Encoding" key. Set it according to your needs.

If you want to change the plugin's config file, navigate to

(menu) Options -> Settings - plugins -> File type profile -> Config

The config file will be opened. Edit its content and save it. In that moment the
plugin will automatically reload the file and update its configuration. Please
note: Only newly opened files will be affected by the updated configuration,
already opened ones will not.

Possible values for the "Encoding" setting you can find in the CudaText wiki,
see here: http://wiki.freepascal.org/CudaText#Encodings

There you also can find the possible values for the "EolFormat" setting, see
here: http://wiki.freepascal.org/CudaText#Line_ends



Author: Andreas Heim (dinkumoil, at github & sourceforge)
License: MIT

```</details>----------
   
   
Name: file URI handler  
Description: Opens file:/// links in CudaText  
<details><summary>readme</summary>
```
Plugin for CudaText.
Opens file:/// links in CudaText, for example:

file:///etc/fstab
file:///c:/WINDOWS/clock.txt
file:///install.inf

Just a filename (last line) will be looked for in the directory of the current file first, then in the directories specified in plugin's config file. 
------------------------------

For CudaText to recognise file urls, 'links_regex' option needs to be changed. For example by adding a line to 'settings/user.json' file:

"links_regex" : "\\b(mailto:)?\\w[\\w\\-\\.]*@\\w[\\w\\-\\.]*\\.\\w{2}\\b|\\b(https?://|ftp://|file:///|magnet:\\?|www\\.|ftp\\.)\\w[\\w\\-\\.@]*:?(:\\d+)?(/[~\\w\\.\\-\\+\\/%]*)?(\\?[^<>'\"\\s]+)?(\\#[\\w\\-]*)?",

------------------------------

Authors:
  @halfbrained (at GitHub)

License: MIT

```</details>----------
   
   
Name: Find in Files  
Description: Gives dialog to search for multiple files containing some string/regex, like in file managers.  
<details><summary>readme</summary>
```
Plugin "Find in Files" for CudaText. Gives dialog to search/replace in multiple files.

- Supports usual search and regex. Regex are from Python, groups are \0...\9.
- Can save current options to "presets".
- Lots of options (much more than in SynWrite).
- Results are shown in editor tab (bottom pane of CudaText not used).
- Can navigate to found lines from result-tab: 
    - using double-click
    - using commands in Plugins menu
    - using "Go to definition" CudaText command

Notes:

- Replace-fields are hidden by default, press the "=" button to show.
- Some opts must be set in user.json, see info after pressing the Help button.
- Files are handled line by line, so can't find/replace multiline matches, with line-end chars.

Author: A.Kvichanskiy (kvichans at forum/github)

```</details>----------
   
   
Name: Find in Files 4  
Description: Gives dialog to search for multiple files containing some string/regex, like in file managers.  
<details><summary>readme</summary>
```
Plugin "Find in Files" for CudaText. Gives dialog to search/replace in multiple files.

- Supports usual search and regex. Regex are from Python, groups are \0...\9.
- Can save current options to "presets".
- Lots of options (much more than in SynWrite).
- Results are shown in editor tab (bottom pane of CudaText not used).
- Can navigate to found lines from result-tab: 
    - using double-click
    - using commands in Plugins menu
    - using "Go to definition" CudaText command

Notes:

- Replace-fields are hidden by default, press the "=" button to show.
- Some opts must be set in user.json, see info after pressing the Help button.
- Files are handled line by line, so can't find/replace multiline matches, with line-end chars.

Author: A.Kvichanskiy (kvichans at forum/github)

```</details>----------
   
   
Name: Find in Files 4  
Description: Gives dialog to search for multiple files (Python 3.5)  
<details><summary>readme</summary>
```
Plugin "Find in Files" for CudaText. Gives dialog to search/replace in multiple files.

- Supports usual search and regex. Regex are from Python, groups are \0...\9.
- Can save current options to "presets".
- Lots of options (much more than in SynWrite).
- Results are shown in editor tab (bottom pane of CudaText not used).
- Can navigate to found lines from result-tab: 
    - using double-click
    - using commands in Plugins menu
    - using "Go to definition" CudaText command

Notes:

- Replace-fields are hidden by default, press the "=" button to show.
- Some opts must be set in user.json, see info after pressing the Help button.
- Files are handled line by line, so can't find/replace multiline matches, with line-end chars.

Author: A.Kvichanskiy (kvichans at forum/github)

```</details>----------
   
   
Name: Focus Mode  
Description: Shades/dims all lines except the current paragraph. Plugin is active only for some lexers, call "Plugins/ Focus Mode/ Config".  
<details><summary>readme</summary>
```
plugin for CudaText.
it shades (dims) all lines except the current paragraph (in which 1st caret placed).
paragraphs should be separated by empty lines.
when caret is on empty line, none is shaded.

it works only for some file extensions.
to configure which file extensions are handled, call menu item "Options / Settings-plugins / Focus Mode/ Config" and edit opened config file (restart CudaText then). you have options in [op] section:

- file_ext: comma-separated list of file extensions.
- dim_value: dim value from 0 (no effect) to 255 (text is transparent). good middle value is 100..150.


author: Alexey T (CudaText)
license: MIT

```</details>----------
   
   
Name: Font Awesome  
Description: Search FontAwesome Icons in sidebar and insert the codes in editor.  
<details><summary>readme</summary>
```
Font Awesome
Plugin for CudaText

Search Font Awesome Icons in sidebar and insert the codes in current editor.

=== IMPORTANT =============================================
Besure you have installed the fonts from vendors/fonts.zip.
===========================================================

Check Plugins -> Font Awesome -> Config for code format.

Default (for HTML):
{
	"code_format": "<i class=\"{font} fa-{name}\"></i> "
}

Possible variables:

{font}    far|fas|fab for Regular, Solid, Brands
{name}    e.g. "address-card"
{unicode} e.g. "\uf2bb"
{hexcode} e.g. "F2BB"

Uses the free version from https://fontawesome.com

Author: Tom Braider
License: MIT

```</details>----------
   
   
Name: Fonts  
Description: Allows to use portable fonts only in CudaText. Fonts are loaded from CudaText data/fonts folder.  
<details><summary>readme</summary>
```
plugin for CudaText.
for Windows only. loads font files, from [CudaText]/data/fonts folder, on CudaText start. it doesn't install fonts into OS.
supports font types: .ttf .ttc .otf .fon

example usage:
- download Fira Code font from web
- copy its files to [CudaText]/data/fonts folder (create this folder)
- restart CudaText
- plugin works, CudaText must see Fira Code font in its "Select text font" dialog, choose this font
- restart CudaText to check that font is active


author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: FontStorage  
Description: In CSS code, inserts usage of external fonts from FontStorage.com site  
<details><summary>readme</summary>
```
plugin for CudaText.
gives menu to work with CSS fonts from site https://fontstorage.com/
it is menu like in similar plugin for Sublime Text.

requires CSS lexer in the current tab, and menu allows to 
a) download font from site to local folder
b) insert CSS lines (at caret position), which correctly refer to downloaded files

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: Fountain Helper  
Description: Helper for Fountain lexer: 1) On Shift+Enter it converts line to upper-case and makes new-line, 2) Command to list dialogs of some character, 3) Command to list all scenes, 4) Command to extract all dialogs of some character, 5) On Ctrl+Space after partial character name it gives auto-completion list, 6) Preview as HTML in browser.  
<details><summary>readme</summary>
```
plugin for CudaText.
it gives features for Fountain lexer:

- event on pressing Shift+Enter: it converts cur line to upper-case and makes a new-line.
- auto-completion list of names, when calling completions (Ctrl+Space) after partial character name.

and commands in "Plugins - Fountain Helper":

- "Character list" 
it finds all character names in cur file, then asks for a name. for entered name, it find all its places and gives menu with these places, to go there. brackets at the end, e.g. "Edward (V.O.)", are stripped. @name and name^ are handled.

- "Character under caret"
it takes name, on separate line, under caret, and shows the dialog like before for this name.

- "Scene list"
it shows list of all scenes, to jump to selected scene. it is the same as using CudaText tree panel on the left, but note: code to find scenes is different, than lexer has for the tree panel.

- "Extract talks of character"
it asks for a name, then finds all talks of that name. talks are collected in a new editor tab, separated by empty lines. 

- "Preview in browser"
it converts current document to HTML (in a temporary folder) and opens HTML file in browser.
this command requires Node.js installed!
it uses parser from: https://github.com/nathanhoad/fountain-js


author: Alexey Torgashin (CudaText)
license: MIT

```</details>----------
   
   
Name: FTP  
Description: Allows to handle remote files/folders on FTP+SFTP servers. Read text file about SFTP support.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Allows to manage remote FTP/SFTP files and directories.
Plugin shows FTP panel in the side panel, with context menu.
Context menu has commands:

Empty list:
 - new server
For servers:
 - new server
 - edit server
 - remove server
 - go to (change ftp directory)
 - new file (creates file in initial dir)
 - new dir (creates dir in initial dir)
 - refresh (re-reads initial dir)
For dirs (after opening server by double-clicking or "refresh"):
 - new file
 - new dir
 - remove dir
 - refresh (re-reads dir)
For files:
 - open file (download and open in editor)
 - remove file
 
Notes

- File, which was downloaded and edited, will be uploaded, when "Save" command runs.
- Config file is "[Cudatext]/settings/cuda_ftp.json"
- No permanent connection to FTP is kept. Each request (read dir, download, upload...) makes new connection, then closes connection.

Read separate text-file about SFTP support.
For SFTP, Paramiko lib must be installed (on Linux and macOS).


Authors: @pohmelie, Alexey T.
License: MIT
Homepage: https://github.com/pohmelie/cuda_ftp

```</details>----------
   
   
Name: Git Status  
Description: Shows Git information in statusbar: current branch name, clean state, etc.  
<details><summary>readme</summary>
```
plugin for CudaText.
for active file tab, it shows information about Git repo, in statusbar in additional cell.

- branch name, e.g. "master"
- * symbol, if this branch is not clean
- +M, for number of commits ahead
- -N, for number of commits behind

ported from GitStatusBar plugin for Sublime Text.
plugin has config-file with few options. to edit it, call menu item "Options / Settings-plugins / Git Status / Config", after editing restart editor.

author: Alexey (CudaText)
license: MIT
icon from GitHub, license: MIT

```</details>----------
   
   
Name: Hash Generator  
Description: Dialog which allows to calculate hash sums (several algorithms) for files/strings  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives dialog, which is similar to PSPad's dialog "Hash generator".

You can calculate hash for a file (choose it from dialog) or for a custom string (string is encoded in ASCII, so Unicode chars not supported).
Also you can paste some known hash string to the bottom input, and it's compared to calculated hash string, by "Verify" button, or after calculating hash value. Label in dialog will show "Verified" or "?".

Currently supported hashes: 

  MD4 (requires OpenSSL lib)
  MD5
  SHA1
  SHA224
  SHA256
  SHA384
  SHA512
  RIPEMD160 (requires OpenSSL lib)
  Whirlpool (requires OpenSSL lib)


Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Hex Dump  
Description: Shows text in hex-dump format  
<details><summary>readme</summary>
```
Command plugin for CudaText.
It converts text from current file (entire file, or only selection, if normal block is selected)
to hex-dump format. And shows hex-dump in a new tab.
Gives commands in "Plugins - Hex Dump":
- Dump UTF16-LE
- Dump UTF16-BE
- Dump ASCII

Used hexdump.py by anatoly techtonik, Public Domain.
Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Highlight Occurrences  
Description: Highlights/Marks all occurrences of current/selected word/fragment  
<details><summary>readme</summary>
```
Plugin for CudaText.
Highlights all occurrences of current word (under caret), or selected text,
with background color. Color is taken from current syntax-theme.
Highlighted fragments can be marked with multi-selections.

To set hotkeys for commands, use F9 functionality in Command palette (Ctrl+Shift+P).
------------------------------

Commands in "Plugins / Highlight Occurrences" menu:

- "Move to first occurrence"
   Move caret to the first highlighted occurrence.
- "Move to last occurrence"
   Move caret to the last highlighted occurrence.
- "Move to previous occurrence"
   Move caret to the previous highlighted occurrence.
- "Move to next occurrence"
   Move caret to the next highlighted occurrence.
- "Select all occurrences"
   Selects (marks with carets) all the highlighted occurrences.
   See plugin setting "mark_ignore_min_len".

------------------------------

Plugin has options dialog, call it by "Options / Settings-plugins / Highlight Occurrences".

Options:
- "min_len"            : (def=2)           : Minimal length of fragment to handle
- "max_lines"          : (def=5000)        : Maximal number of lines in document (plugin will disable highlight functionality)
- "max_line_len"       : (def=500)         : Maximal length of lines, which will be handled by plugin (plugin will skip longer lines)
- "sel_allow"          : (def=True)        : Plugin handles current selection (on selection changing)
- "sel_allow_spaces"   : (def=False)       : Plugin allows whitespace in selection, otherwise trim it
- "sel_case_sens"      : (def=False)       : Search for selection is case-sensitive
- "sel_words_only"     : (def=False)       : Plugin handles selection only when it is whole word
- "sel_whole_words"    : (def=False)       : Search for selection finds whole words only
- "mark_ignore_min_len": (def=False)       : Mark occurrences of selected text ignores 'min_len' option. Related to "Plugins / Highlight Occurrences / Select all occurrences" option
- "caret_allow"        : (def=True)        : Plugin handles word under caret (on caret moving)
- "caret_case_sens"    : (def=True)        : Search for word under caret is case-sensitive
- "caret_whole_words"  : (def=True)        : Search for word under caret finds whole words only
- "theme_item_current" : (def="BracketBG") : Element of syntax-theme, which color is used for word under caret
- "theme_item_other"   : (def="BracketBG") : Element of syntax-theme, which color is used for other found matches
- "lexers_allowed"     : (def="")          : If not empty, plugin is active only for mentioned lexers. Comma-separated list, None-lexer must be written as '-'
- "lexers_disabled"    : (def="")          : If not empty, plugin is disabled for mentioned lexers. Comma-separated list, Has higher priority than option 'lexers_allowed'.

Authors:
  Alexey Torgashin (CudaText)
  @myCrack (at GitHub)
  @Jairo-Martinez (at GitHub)

License: MIT

```</details>----------
   
   
Name: Highlight Variables  
Description: Highlights "variables" inside strings literals (for Bash lexer, etc)  
<details><summary>readme</summary>
```
plugin for CudaText.
it performs work additional to lexer: highlights "variables" (e.g. in Bash script it's $var or ${var_long}) inside string literals. lexer cannot do this, it highlights string literals with single color.

plugin has config file, call menu item "Options / Settings-plugins / Highlight Variables".
config file has sections [lexer_name] with lexer names.
plugin has predefined config for "Bash script" and "Perl":

[Bash script]
regex_str=".*?"
regex_var=\$\w+|\$\{.*?\}
color=IdVar

items:
- reg.ex. for string literal,
- reg.ex. for variable inside string literal,
- color-id from theme. to see possible color-ids, open CudaText dialog Options / Settings-more / Settings-theme-syntax. also good to use color-id IdVar, it's used for variables outside of strings, but (in default theme) it's greenish color similar to string color.

author: Alexey Torgashin (CudaText)
license: MIT

```</details>----------
   
   
Name: HTML Completion  
Description: Handles auto-completion (Ctrl+Space) in HTML/PHP files. 1) Auto-completion with file names, when caret is inside IMG tag. 2) Auto-completion with CSS class/id names, when caret is inside 'class=""' or 'id=""'.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Auto-completion plugin, it handles Ctrl+Space command in HTML/PHP files.
Lexer name can be PHP or any name beginning with "HTML". 

1) Auto-completion of CSS class names, while editing HTML "class" and "id" attributes of tags.

Examples:
- If HTML file links to "main.css" and "main.css" defines n class names 
  (for specific tags, or general names for all tags), then HTML editor will show
  these n names while you call auto-completion after "class" attrib. 
  <table class="|" >
- Same for "id" attribs, if css-file contains such id's.
  <div id="|">

CSS may be linked in HTML in such ways:
- with <link type="text/css" href="main.css" rel="stylesheet">
- with <style type="text/css"> styles here... </style>
- with <style type="text/css"> @import "main.css"; </style>


2) Auto-completion of picture file names, when caret is inside "src" value:
<img src="|">.
It handles partially typed filenames, and folder (with sub folders) names.
Supported file extensions: png, gif, jpg, jpeg, ico, bmp.


Authors:
  Alexey T. (CudaText)
  Artem Gavrilov (@Artem3213212)
License: MIT

```</details>----------
   
   
Name: HTML Live Preview  
Description: Provides live preview for HTML files with support of dynamically linked sources  
<details><summary>readme</summary>
```
Plugin for CudaText.
Allows to use live preview of HTML and Markdown files in the browser, during editing, without need to reload browser page.
Requires Python 3, Flask framework and Markdown2 library.
Tested on Windows 10 and Linux (Ubuntu 19).

How to use
----------

- Install Python 3 from official site. With adding it to PATH variable. 
- Install Flask in Python.
  Run in terminal:
    pip install flask
    pip install markdown2
  on Unix:
    pip3 install flask
    pip3 install markdown2

- In CudaText, specify path to browser: "Plugins / HTML Live Preview / Config".
  For example: "chrome", "firefox", "opera" or full path to executable file.
  Restart CudaText.

- In CudaText, call "Plugins / HTML Live Preview / Start server".
  This should show terminal with running Flask server.
  Browser should open at http://127.0.0.1:5000/view

After that, just edit some HTML file.
Server will detect your changes (after last editing, make small pause)
and browser should show the preview.

Lexer names handled: any with "HTML", "Jinja2" and "Markdown".

Note: on clicking any link in the browser, live preview stops, until you return to the 
http://127.0.0.1:5000/view


Browsers
--------

Supported:
- Google Chrome
- Firefox
- Opera
- Microsoft Edge 42

Not supported:
- Internet Explorer


About
-----
Authors:
  Medvosa, https://github.com/medvosa
  Alexey Torgashin (CudaText)
License: MIT

```</details>----------
   
   
Name: HTML Ops  
Description: Commands to work with HTML/CSS  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives commands for HTML/CSS work (lexer name can be any).

--------------------------  
* commands to preview current HTML text in web browser.
  2 commands (new tab/ new window) for current browser and per each major browser 
  (Firefox/Chrome/Safari/Opera/Windows-default).
  
  for selection, only selection is previewed, and a temp-file is created (_cudatext_preview.html),
  in the same folder as original file (so temp file can see relative HTML links).

--------------------------  
* commands to wrap selection in HTML tag.
  commands for about 25 tags.
  e.g. "text" -->  "<b>text</b>"

--------------------------  
* command, to do the same as Sublime Text does on hotkey Alt+Shift+W:

  on selection: wrap selection with <p></p> and place 2 selections to rename tag
  w/o selection: add <p></p> with 2 selections and 2 markers:
    1st TAB press goes into tag,
    2nd TAB press goes after tag

--------------------------
* command "HTML selection to CSS classes":
  finds fragments 'class="name"' in selected block, and generate list (sorted) of CSS classes from this block. resulting list is copied to clipboard, to paste to CSS file. example of result:

.first {  }

.somemore {  }

.another {  }

--------------------------  
* command, which converts selected value between "px" and "rem" units.
  it works only if selection is number + "px" or "rem", and changes selection
  between "px" and "rem" value. it leaves only 4 digits of float-number after dot.
  for ex, 10px -> 0.625rem -> 10.0px.
  idea: user "nmsalinas", site: www.nevermindhttp.com

--------------------------  
* function of plugin "HTML Image Tag".
  Command to choose image file (jpeg, png, gif), and inserts image info into code. 

  For CSS lexer (and several CSS based lexers: scss, sass, stylus) it inserts such text:

    background: url("path/file.png");
    width: 70px;
    height: 70px;

  For other lexers (assumed it's HTML) it inserts HTML <img> tag:

    <img src="path/file.png" width="70" height="70" alt="untitled" />

  It replaces full path of image to short path "fn.png" or "subfolder/fn.png"
  if image file is in the editor file's subfolder.

--------------------------  
* function of plugin "HTML Lines To List". 
  commands "Convert lines to list", convert several selected lines to:
  - ordered list <ol> ... </ol>    
  - unordered list <ul> ... </ul>
  - table <table>, arrange cells by lines    
  - table <table>, arrange cells by columns
      
--------------------------
* function of plugin "HTML Validator".
  Items to check current document via online checkers: HTML4/HTML5.
  Automatic format detection often fails, so you have to manually choose it.
  It shows results in Validate panel (in the bottom panel), you can double-click result 
  lines to go to error.

--------------------------
* function of plugin "Increment".
  2 commands to increase/decrease number under caret. 
  Numbers in CSS/HTML supported: 100px, 1.200em. 
  Float numbers supported (dot must be used).
  Multi-carets supported: all numbers for all carets affected.

--------------------------
* event for HTML lexers (any lexer name with "HTML" word):
  Enter key press between opening/closing tag, makes smart indent:

    <tag>|</tag>
    converts to
    <tag>
      |
    </tag>
  
    <a href="#GlossTop">|Top</a>
    converts to
    <a href="#GlossTop">
      |Top
    </a>
  

Author: Alexey T. (CudaText)
License: MIT

```</details>----------
   
   
Name: HTML Tidy  
Description: Validates HTML documents using Tidy tool  
<details><summary>readme</summary>
```
CudaText plugin to integrate HTML Tidy program.
HTML Tidy is a program, which helps to find errors in HTML documents and to perform some actions on HTML pages, such as "convert tags to lowercase", "convert document to XHTML form", "make document clean", "reformat for better readability" etc.

- Windows: plugin includes 32-bit program Tidy.exe
- Unix: you must install "tidy" package in your OS

Plugin adds menu items to "Plugins" menu:
- "Menu": shows list of configured Tidy actions. Each action formats source file, if it's ok; if not it shows error report in Validation tab of bottom panel.
- "Validate document": shows list of errors in code in Validation tab of bottom panel. You can double-click lines in this list to go to source code.
- "Browse configs": shows folder with config files, one txt file per Tidy action, you can edit configs or add new ones.

Help links:
- http://tidy.sourceforge.net/docs/quickref.html - HTML4 Tidy help
- http://w3c.github.io/tidy-html5/ - HTML5 Tidy help

Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: HTML Tooltips  
Description: In HTML/CSS files, plugin shows tooltips for: HTML color values, HTML entities, picture filenames  
<details><summary>readme</summary>
```
Plugin for CudaText.
It works in HTML/CSS files (any lexer name with words "HTML", "CSS").
When you move mouse cursor over some fragments, tooltip appears.

1) It finds HTML color values: 
  #RGB 
  #RRGGBB
  rgb(n, n, n)
  rgba(n, n, n, n)  
  and adds colored tooltips for them.
2) It finds HTML picture refs: src="..." or href="..."; and adds picture tooltips for filenames.
  Internally, it finds any quoted picture filenames (png, gif, jpeg, bmp, ico) without testing tags.
  Online links (http:, https:) are not supported.
3) It finds HTML entities like &copy; &amp; etc, and adds Unicode tooltips for them.

It finds filenames in CSS files in special format: in brackets, not in quotes.
To tell plugin, which lexers are CSS based, edit:
- install.inf, field "lexers=" (option is in install.inf to speedup app on other files)
- plugin option "lexers_css", it's in config file.

To edit config, call "Options/ Settings-plugins/ HTML Tooltips/ Config".

It finds fragments:
- on opening file,
- after text is changed + pause passed (CudaText option "py_change_slow").

If you're interested, what is HSL display, see
https://www.rapidtables.com/convert/color/rgb-to-hsl.html


Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Insert Emoji  
Description: Dialog with list of most common emojis (about 900), to insert emoji name like :smile:  
<details><summary>readme</summary>
```
plugin for CudaText.
it shows list of common emoji with pictures (about 880 items in list).

- Enter key: insert emoji selected in listbox, like :smile:. supports multi-carets.
- Esc key: cancel dialog.
- text keys, digits, BackSpace: edit filter string (it's shown on top of dialog). filter string leaves only items, which contain filter.


emoji list+icons are taken from 
https://www.webpagefx.com/tools/emoji-cheat-sheet/

author: Alexey T (CudaText)
license: MIT

```</details>----------
   
   
Name: Insert Pics  
Description: Allows to insert preview of pictures (png/jpeg/gif/bmp/ico) into text. Saves pictures in helper file, to automatically load pics on file re-opening.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives the ability to insert picture files (PNG/JPEG/GIF/BMP/ICO) to inter-line gaps,
so pictures will be shown between lines. This works for any file and any syntax
(with plain-text too).

Plugin gives commands in "Plugins / Insert Pics" menu:
- Insert pic
- Remove pic for current line
- Remove all pics

Prompt to resize is shown, if width of picture is bigger than ~500 px.
Picture is auto-resized, if height is bigger than ~500 px.

When file with picture(s) is saved, plugin creates helper file with extention .cuda-pic,
in the same folder. It is JSON file with info about inserted pictures.
Pictures are saved in the helper file, in Base64 encoding, so helper file is big.
On opening original file later, plugin reads the helper file, and re-adds pictures from it.
It creates picture files in the OS temp folder.

During editing, if you insert/delete lines, pics are glued to their original lines.
They're deleted only if you delete their lines, or use plugin's commands to delete pics.


Author: Alexey Torgashin (CudaText)
License: MIT

```</details>----------
   
   
Name: In-text bookmarks  
Description: Allows to place bookmarks as text-comments (permanent bookmarks), and to navigate to them  
<details><summary>readme</summary>
```
Plugin for CudaText.
Allows to manage bookmarks which are text-comments of special kind.
Can add, show list, jump to bookmarks.

Author: Andrey Kvichanskiy (kvichans, at forum/github)
```</details>----------
   
   
Name: In-text complete  
Description: Suggests completions for syntax expressions, using fragments from the entire text  
<details><summary>readme</summary>
```
Plugin for CudaText.
Allows to complete expression (word, calling, ...) by variants found in the whole text.

Author: Andrey Kvichanskiy (kvichans, at forum/github)
```</details>----------
   
   
Name: IP Address Helper  
Description: When mouse hovers IP address in text, plugin shows country of that address in the statusbar  
<details><summary>readme</summary>
```
plugin for CudaText.
on hovering mouse over IP address, plugin shows country of that IP in the statusbar.
eg, "IP: United States". requires online state. on connection error, shows "IP: ?".
supports IPv4 and IPv6 addresses.

author: Medvosa (at GitHub)
license: MIT

```</details>----------
   
   
Name: JS Multiline Array  
Description: Converts several selected lines of text - to JavaScript string array  
<details><summary>readme</summary>
```
Plugin for CudaText
It reads current selection (only 1 caret allowed) and converts it to JavaScript array of string,
with "join". Example of result:

['dddd',
'ddddddddd',
'aaaa'].join('\n');

You can a) replace selection with JS code, b) copy JS code to clipboard.
Commands are in Plugins menu.

Converter code (few lines) from https://github.com/metatribal/sublime-jsmultiline
License for this plugin: Apache 2.0 or MIT
Author: Alexey T. (CudaText)

```</details>----------
   
   
Name: JS Tern  
Description: Gives intelligence commands for JavaScript: 1) auto-complete (Ctrl+Space), 2) go-to-definition (item in context menu), 3) show function call-tip, 4) show doc-string, 5) show usages. Based on Tern engine, requires Node.js.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives intelligence commands for JavaScript, using Tern engine, http://ternjs.net/

1) Auto-completion (Ctrl+Space)
2) Go-to-definition (command item in editor context menu)
3) Show function call-tip (Ctrl+Shift+Space, info will show at the editor bottom)
4) Show doc-string (comment above function/class/var definition, info will show in the Output panel)
5) Show usages (list of places where name is used, with go-to after selecting item)

======================================
First, you must install Node.js engine, then install Tern like this:
  [sudo] npm install tern -g

Lexer name "JavaScript" is set in the file install.inf, you may append names of other JS-based lexers, after comma.

======================================
For complex code with some files, with "require" JS commands, you must make a project!
To create a project, install "Project Manager" CudaText plugin and open its panel, then create a project, add to project your JS files (tested with js files in one folder). Save resulting project file (name.cuda-proj) to the same folder as JS files. This project must be opened (in Proj Manager) before calling auto-completion/ go-to-definition, else Tern will not find other JS files (so no completions for functions from other files). Plugin makes simple .tern-project file to help Tern.


Authors:
- https://github.com/pohmelie/
- Alexey T. (CudaText)
    
License: MIT

```</details>----------
   
   
Name: Lorem Ipsum  
Description: Inserts "Lorem Ipsum" text (placeholder for HTML pages)  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives dialog to insert "lorem upsum" (standard template) text.
Can insert N sentences (dot-separated), or N paragraphs (blank line separated) or N paragraphs separated by <p> HTML tags.
N is the option in the dialog.
Multi-carets are supported, text will be inserted at multi-carets.

Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Macros  
Description: Macros manager for CudaText. Gives commands to record/playback/save/delete/etc macros.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Macros manager for CudaText. Gives commands to record/playback/save/delete/etc macros.

Config and data file:
	settings\macros.json

Author: Andrey Kvichanskiy (kvichans, at forum/github)
```</details>----------
   
   
Name: Markdown Editing  
Description: Helpers for editing Markdown documents  
<details><summary>readme</summary>
```
Plugin for CudaText.
Supports features during editing of Markdown documents.

Symbols *_` (asterisk, underscore, tick)
  - auto-paired on typing
  - if they are typed with selected text, selection is enclosed in symbols pair
  - with pair of symbols, and BackSpace pressed - both symbols are deleted
  - with pair of symbols, and Space pressed - right symbol is deleted

List items (bullet symbol -+* with space)
  - if caret at the end of non-empty list item, and Enter pressed - newline is added with empty list item (on the same indent as previous item)
  - if caret at the end of empty list item, and Enter pressed - bullet is deleted and caret goes to bullet position
  - after empty list item, and Tab pressed - list item's indent is increased, and bullet kind is changed (by loop: +-*)
  - after empty list item, and Shift+Tab pressed - list item's indent is decreased, and bullet kind is changed

Tasks
  - [x] foo
    - [x] baz
  - [ ] bim
  if caret at the end of a task, and Enter pressed - newline with empty unchecked task is added.

Block-quotes
  - if caret at the end of quoted line, and Enter pressed - newline with quote symbol is added
  - if text is selected, and > pressed - selection is enclosed in block-quote. First and last lines of multiline selection must not be fully selected. Single line must not be fully selected.

Links
  - if text selected, and ( or [ pressed - selection is enclosed into pair () or []

Crossed text
  - if text selected, and ~ pressed - selection is enclosed like this: ~~text~~

Headers
  - if text selected (single line), and # pressed - # symbol is added in front of selection. If plugin option "match_header_hashes" is on - # symbol mirrors to the end of header. Next # presses will increase header level (##, ###, up to level 6, then # symbols removed).
  - if caret at the and of header, and Enter pressed, and option "match_header_hashes" is on - # symbols are mirrored
  - Setext headers (text with --- or === underline on the next line) - pressing Tab at the end of underline - changes underline length to match the length of header text


Plugin has config file, section [markdown_editing] in "plugins.ini".
You may open config via "Options / Settings-plugins / Markdown Editing / Config".
Options:
  - list_indent_bullets - allowed bullets (from +-*), for changing bullet kind; for ex, value "-+" means only -+ bullets
  - match_header_hashes - boolean, 0/1 - allows to mirror leading # symbols to the end of header


Authors:
  Medvosa, https://github.com/medvosa
  Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Markdown Preview  
Description: Previews Markdown text as HTML page in browser  
<details><summary>readme</summary>
```
Plugin "Markdown Preview" for CudaText.
It converts Markdown text to HTML (using Python library), and then opens HTML file in browser. 

You can use file "cuda_markdown_options.py" to init set of Markdown extensions. 
Values listed at: 
https://pythonhosted.org/Markdown/extensions/#officially-supported-extensions


Author: Alexey T.
License: MIT

```</details>----------
   
   
Name: Micro Utils  
Description: Minor commands to work with bin/hex numbers, etc  
<details><summary>readme</summary>
```
plugin for CudaText.
small commands to work with binary/hex numbers, etc.

Binary Sum
==========
for any decimal or hex number (64 bit currently, use "0x" prefix for hex), it decomposes number to the sum of 2^N for some indexes N.
for example:
  112 (0x70)
  = 16 + 32 + 64
  bits 4 5 6


Convert base-2 to hex
=====================
stackoverflow.com
E.g. I have a file with the following lines:
00000000000000000000000000001000, 00000000000000000000000000000000, 00000000000000000000000000010000, 00000000000000000000000000111000, 00000000000000000000000000110000, 00000000000000000000000001000000,
And I want to see them in hex representation:
0000_0008, 0000_0000, 0000_0010, 0000_0038, 0000_0030, 0000_0040,

Command reads current text as a list of base-2 nums (separators: , ; space tab newline),
converts them to list of hex NNNN_NNNN, writes result to a new tab.


Sort lines by length
====================
Sorts all lines in the current editor. First go short lines, then longer. Same len lines sorted by text.


author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: NTFS Streams  
Description: Allows to work with NTFS file streams (Windows)  
<details><summary>readme</summary>
```
plugin for CudaText.
gives dialog which allows to work with Windows NTFS file streams (ADS).

dialog works with streams of currently active file:

- choose existing stream and open it in CudaText, like a file with name original_name:stream, ie stream name is appended to filename after ":" char.
- add new empty stream with given name
- add new stream from given existing file (store this file into stream)
- delete any stream

author: Alexey T (CudaText)
license: MIT

```</details>----------
   
   
Name: Number Utils  
Description: Commands for numbers: insert row of numbers, convert to text or Romans, etc.  
<details><summary>readme</summary>
```
plugin for CudaText.
merged several plugins, which give number-related commands.


Insert Numbers
--------------
dialog to insert numbers: from starting number, with increment (default 1), with prefix/suffix strings.
- only one caret allowed.
- if selection exists, then selected lines will be numbered, at line start.
- if no selection, then "repeat counter" field is enabled in dialog, numbers are inserted at start of caret's line.


Carets Numbering
----------------
works only with multi-carets, allows to insert increasing/decreasing numbers in positions of all multi-carets.
for example, you can insert:
- 00, 01, 02, 03...
- 0030, 0031, 0032...
- 100, 95, 90, 85...

gives dialog to input parameters:
- Starting number (default is 1)
- Increment (use value<0 to make decreasing numbers)
- Number of digits, ie width of numbers (if it's 3, numbers can be 001, 002, 003...)
- Text before numbers (prefix)
- Text after numbers (suffix)
- Base: 
  - "d": decimal format
  - "x": hex format
  - "o": octal format
  - "r": Roman notation


Romanize
--------
converts number (in the current editor under first caret) between decimal and Roman formats.
plugin reads an entire word at caret, and tries to convert it.

Roman numbers can have only digits: IVXLCDM, lowercase digits are allowed.
numbers<=0 are not supported.
result is not nice for numbers >=4000.

gives commands:
- Show: convert number between decimal/Roman, and show it in the statusbar
- Replace: the same, and replace number in the editor


Number to Words
---------------
converts number (under caret) into textual form, e.g.
- "10" -> "ten"
- "2030" -> "two thousand and thirty"
works with integer and floating numbers.
floating point can be "." and ",".

gives commands:
- read number under caret, put result to a new tab
- read number under caret, replace this number with result
- select language


Number to Words, Ru
-------------------
converts number (under caret) into Russian textual form, e.g.
- "10" -> "десять"
- "2030" -> "две тысячи тридцать"
works with integer and floating numbers.
floating point can be "." and ",".

gives commands:
- number to words, put to new tab
- number to words, replace
- roubles to words, put to new tab
- roubles to words, replace


authors:
  Alexey Torgashin (CudaText)
  Jairo Martinez Antonio https://github.com/Jairo-Martinez
license: MIT

```</details>----------
   
   
Name: Numbered Bookmarks  
Description: Allows to set and go to numbered bookmarks (1..8)  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives commands to
- Place numbered (1..8) bookmarks on line with the first caret.
- Go to given numbered bookmark.

Numbered bookmarks behave like usual bookmarks, but they have special icon (with number) on the gutter, and only one bookmark with each index can be placed.

License: MIT
Author: Alexey (CudaText)

```</details>----------
   
   
Name: Online Search  
Description: Opens webbrowser with search for selection/word, supports several search engines  
<details><summary>readme</summary>
```
plugin for CudaText.
gives several commands to call online (www) search engines, for currently selected text (Google, Bing, Wikipedia) or for current word (programming docs).
commands open web-browser with search results.

- Wikipedia
- Google
- Bing
- HTML doc
- HTML5 doc
- MSDN
- PHP.net
- Laravel Docs

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: Open URL  
Description: Gives commands to open URL (under text caret) in many browsers  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives menu "Plugins / Open URL" with several commands to open URL (under first caret in editor) in browser. Commands:

- Chrome
- Chrome, private (incognito) mode
- Firefox
- Firefox, private mode
- Opera
- Opera, private mode
- IE
- IE, private mode

Plugin also handles double-click event in editor, and if URL is double-clicked, it shows menu to open this URL.

You can configure paths to browsers, using config file - to edit file, call menu "Options / Settings-plugins / Open URL".

Option "handle_click": boolean (0 or 1): enable action of clicking URL in text.
Option "action_on_click": number:
- If -1: click on URL shows menu of browsers to use
- If >=0: it's 0-based index of menu item in browsers menu, this choice is used instead of showing menu.


Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Options Report  
Description: Shows HTML page with report of options  
<details><summary>readme</summary>
```
Plugin for CudaText.
Shows detailed report about options, as HTML file, in browser.

Author: Andrey Kvichanskiy (kvichans, at forum)

```</details>----------
   
   
Name: Pandoc Helper  
Description: Uses Pandoc tool, to convert several markup formats to output formats, which Pandoc supports (Word, PDF, Markdown etc)  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives command to call Pandoc tool, to convert current file to some format, which Pandoc supports.

Input format: detected by active lexer name, or, if unknown lexer, menu will be shown.
Output format: menu is always shown.

Notes:
- Plugin needs saved file, cannot handle unsaved text yet.
- Resulting file is made in the OS temp-folder, you will see filename after converting done.
- PDF is supported by Pandoc only with some additional tool (Latex), else you will see error message on converting to pdf.

Pandoc program name:
- Windows: pandoc.exe, w/o folder, so you should add it to system PATH.
- Linux: pandoc
- macOS: /usr/local/bin/pandoc


Author: Alexey T. (CudaText)
License: MIT

```</details>----------
   
   
Name: Password Generator  
Description: Generating a random password of a certain length from certain characters  
<details><summary>readme</summary>
```
Plugin for CudaText
Generating a random password of a certain length from certain characters

Aauthor: ildar r. khasanshin (10021987.ru)
License: MIT
```</details>----------
   
   
Name: Paste as String  
Description: Pastes text from Clipboard as "string" for current lexer  
<details><summary>readme</summary>
```
Plugin for CudaText
Generating a random password of a certain length from certain characters

Aauthor: ildar r. khasanshin (10021987.ru)
License: MIT
```</details>----------
   
   
Name: Plain Tasks  
Description: ToDo-list plugin for CudaText  
<details><summary>readme</summary>
```
Plain Tasks plugin for CudaText

Installation

    install lexer ToDo (required by plugin, not included in this repo)
    install plugin Plain Tasks

Projects

    Anything with colon at the end of the line is a project title
    Projects can be nested inside each other
    Projects can be folded (a built-in editor feature)

Work with tasks
Create tasks

    command: Plain Tasks/New adds a new task
    Alt+I also adds a new task
    If you’re on a new line, plugin creates a new task on the current line
    If you’re on a line with a task, pressing new task shortcut adds a task after it
    If you’re on a line with some normal text, pressing new task shortcut converts it to a task
    New tasks are nested as much as the task on the previous line
    If option "add_created_tag"=true, also add tag @created with timestamp

Complete tasks

    command: Plain Tasks/Complete marks a task as done @done(19-12-24 01:10)
    Alt+D also marks a task as done @done(19-12-24 01:06)
    Pressing Alt+D again puts it back in pending mode
    If option "done_tags"=true, also add tag @done
    If option "done_date"=true, also add timestamp

Cancel tasks

    command: Plain Tasks/Cancel marks the task as cancelled @cancelled(19-12-24 01:12)
    Alt+C marks the task as cancelled @cancelled(19-12-24 01:12)
    Pressing Alt+C again puts it back in pending mode
    If option "done_tags"=true, also add tag @cancelled
    If option "done_date"=true, also add timestamp

Tagging tasks

    You can add tags using @ sign, like this @tag

Archiving tasks

    command: Plain Tasks/Archive archives tasks in done mode (completed or cancelled tasks).
    Alt+Shift+A archives tasks in done mode (completed or cancelled tasks).
    It does it by removing them from your list and appending them to the bottom of the file under Archive project.
    The archive project is separated from the other list of projects with a line. See bottom of this file.

Priority

    type c, press Tab key — it’ll become @critical
    type h, press Tab key — it’ll become @high
    type l, press Tab key — it’ll become @low
    type t, press Tab key — it’ll become @today

Time tracking

    type s, press Tab key — it’ll become @started(19-12-24 01:22). You’ll get a current date and time; When a task with such tag is completed/cancelled, plugin will calculate the time spent on that task.
    type tg, press Tab key — @toggle(14-10-13 16:14). That way you can pause and resume started task, so result of calculation will be more correct. First, you need start task, then toggle means pause, next toggle — resume, etc.
    type cr, press Tab key — @created(14-12-24 15:57).

File types

Plugin supports these file types out of the box:

    TODO
    *.todo
    *.todolist
    *.taskpaper
    *.tasks

Settings

To configure plugin, call menu item "Options / Settings - plugins / Plain Tasks / Config..."

About

    Author: OlehL, https://github.com/OlehL
    License: MIT

```</details>----------
   
   
Name: Python IntelliSense  
Description: Supports intelligence commands for Python: 1) auto-completion (Ctrl+Space), 2) goto-definition (item in context menu), 3) show function call-tip (Ctrl+Shift+Space), 4) show function doc-string, 5) show usages of name. Based on Jedi library.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives intelligence commands for Python lexer.

*  Auto-completion.
   To use it: place caret after incomplete function/class/variable/module name,
   and call CudaText command "auto-completion menu" (Ctrl+Space).

*  Go to definition.
   To use it: place caret on a name of function/class/variable/module, and call
   CudaText command "go to definition" (or use menu item "Go to definition"
   in the editor context menu, or use mouse shortcut).

*  Show function call-tip.
   To use it: place caret after function name between () brackets, and call
   CudaText command "show function-hint" (Ctrl+Shift+Space).
   For example, enter such script, caret is shown as "|":
     import os
     fn = os.path.join(|)
   Command will show the parameters of "os.path.join" in the floating panel
   at the top of CudaText window.

*  Plugin command "Show function doc-string".
   Shows doc-string for function/class name under caret, in the Output panel.
   (To call Output panel, click on the lower part of CudaText sidebar.)

*  Plugin command "Show usages".
   Shows menu with locations (file name, line number) where identifier under caret
   is used. After choosing the item in menu, editor jumps to chosen location.


Refactoring commands, they change editor text:

*  Refactoring - Rename
   Renames all instances of identifier under the caret.
*  Refactoring - Inline
   Inlines a variable under the caret. This is basically the opposite
   of extracting a variable.
*  Refactoring - Extract variable
   Moves an expression to a new statemenet.
*  Refactoring - Extract function
   Moves an expression to a new function.

Plugin handles CudaText projects (internally calling Project Manager plugin).

Based on Jedi library:
  Jedi is a static analysis tool for Python that can be used in IDEs/editors.
  https://github.com/davidhalter/jedi

Authors:
  Alexey Torgashin (CudaText)
  Oleh Lutsak https://github.com/OlehL/
License: MIT

```</details>----------
   
   
Name: pywin32 libraries  
<details><summary>readme</summary>
```
Library "pywin32" and its requires libraries.
From https://github.com/mhammond/pywin32/releases
for Python 3.6.

Additional python wrapper is taken from Sublime Text addon "TextToSpeech".

Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Remove Greek Accents  
Description: Replaces Greek letters with accents - to similar letters without accents  
<details><summary>readme</summary>
```
plugin for CudaText.
the idea is from Sublime Text plugin.
https://packagecontrol.io/packages/RemoveGreekAccents
original description:

  Using ST3 built-in “Convert to Upper Case” for Greek is not very convenient
  since capital letters in Greek don't require accents. It's easy to change from
  Ελληνικά to ΕΛΛΗΝΙΚΆ but then you need to change ΕΛΛΗΝΙΚΆ to ΕΛΛΗΝΙΚΑ, which
  means more typing. This package automates the process of removing accents from
  your selection.

CudaText plugin gives one command. it handles the selection, or entire text if nothing selected.

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: reStructuredText Preview  
Description: Previews reStructuredText file as HTML page in browser  
<details><summary>readme</summary>
```
plugin for CudaText.
works with lexer reStructuredText (reST).
converts active editor tab (with lexer reST) into HTML document, opens HTML in web-browser.

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: Session Manager  
Description: Allows to manage "sessions" in editor  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives commands in menu "Plugins" to manage sessions. Session is a set of opened named documents, with properties of each document: caret position, encoding, lexer, bookmarks etc. Session also contains information how "editor groups" are placed/resized. Sessions are stored to files in JSON format, with .cuda-session extension, usually in the "settings" folder of CudaText.

Plugin also supports session files from SynWrite editor, which have different format and .synw-session extension.

Plugin commands:
- Recent sessions: Show last used sessions in menu-dialog, and open chosen session.
- Open/New session: Show "Open" dialog to open session file (create session if filename not exists).
- Open previous session: Open most recently used session.
- Close session: Forget name of current session.
- Forget session and close all files: Forget name of current session, and close all documents.
- Save session: Save current session (CudaText does it only on app closing).
- Save session as: Save current session to a new file.

Author: Andrey Kvichanskiy https://github.com/kvichans/
License: MIT

```</details>----------
   
   
Name: SFTP support for FTP plugin, Windows x32/x64, Python 3.5  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives commands in menu "Plugins" to manage sessions. Session is a set of opened named documents, with properties of each document: caret position, encoding, lexer, bookmarks etc. Session also contains information how "editor groups" are placed/resized. Sessions are stored to files in JSON format, with .cuda-session extension, usually in the "settings" folder of CudaText.

Plugin also supports session files from SynWrite editor, which have different format and .synw-session extension.

Plugin commands:
- Recent sessions: Show last used sessions in menu-dialog, and open chosen session.
- Open/New session: Show "Open" dialog to open session file (create session if filename not exists).
- Open previous session: Open most recently used session.
- Close session: Forget name of current session.
- Forget session and close all files: Forget name of current session, and close all documents.
- Save session: Save current session (CudaText does it only on app closing).
- Save session as: Save current session to a new file.

Author: Andrey Kvichanskiy https://github.com/kvichans/
License: MIT

```</details>----------
   
   
Name: SFTP support for FTP plugin, Windows x32/x64, Python 3.6  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives commands in menu "Plugins" to manage sessions. Session is a set of opened named documents, with properties of each document: caret position, encoding, lexer, bookmarks etc. Session also contains information how "editor groups" are placed/resized. Sessions are stored to files in JSON format, with .cuda-session extension, usually in the "settings" folder of CudaText.

Plugin also supports session files from SynWrite editor, which have different format and .synw-session extension.

Plugin commands:
- Recent sessions: Show last used sessions in menu-dialog, and open chosen session.
- Open/New session: Show "Open" dialog to open session file (create session if filename not exists).
- Open previous session: Open most recently used session.
- Close session: Forget name of current session.
- Forget session and close all files: Forget name of current session, and close all documents.
- Save session: Save current session (CudaText does it only on app closing).
- Save session as: Save current session to a new file.

Author: Andrey Kvichanskiy https://github.com/kvichans/
License: MIT

```</details>----------
   
   
Name: SFTP support for FTP plugin, Windows x32/x64, Python 3.7  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives commands in menu "Plugins" to manage sessions. Session is a set of opened named documents, with properties of each document: caret position, encoding, lexer, bookmarks etc. Session also contains information how "editor groups" are placed/resized. Sessions are stored to files in JSON format, with .cuda-session extension, usually in the "settings" folder of CudaText.

Plugin also supports session files from SynWrite editor, which have different format and .synw-session extension.

Plugin commands:
- Recent sessions: Show last used sessions in menu-dialog, and open chosen session.
- Open/New session: Show "Open" dialog to open session file (create session if filename not exists).
- Open previous session: Open most recently used session.
- Close session: Forget name of current session.
- Forget session and close all files: Forget name of current session, and close all documents.
- Save session: Save current session (CudaText does it only on app closing).
- Save session as: Save current session to a new file.

Author: Andrey Kvichanskiy https://github.com/kvichans/
License: MIT

```</details>----------
   
   
Name: Show Unicode Name  
Description: Shows full Unicode name of a character under first caret, in the statusbar  
<details><summary>readme</summary>
```
plugin for CudaText.
shows Unicode full name (e.g. "LATIN CAPITAL E") for character under first caret.
shows it in the statusbar in a separate cell, on the right side.
seems it doesn't slow down editor (on 2010 year average PC).

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: Snippets  
Description: Snippets engine, described in CudaText wiki. Snippets are expanded by Tab-key or can be called from menu.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Snippets engine, which is described in CudaText wiki:
https://wiki.freepascal.org/CudaText_plugins#Snippets

Now plugin also supports snippets from VS Code.
It gives the command to install snippets from VS Code repositories.
This big rework was done by @OlehL.
This includes support of TextMate snippet macros:

- TM_SELECTED_TEXT
- TM_CURRENT_LINE
- TM_CURRENT_WORD
- TM_LINE_INDEX
- TM_LINE_NUMBER
- TM_FILEPATH
- TM_DIRECTORY
- TM_FILENAME
- TM_FILENAME_BASE
- CLIPBOARD
- WORKSPACE_NAME
- CURRENT_YEAR
- CURRENT_YEAR_SHORT
- CURRENT_MONTH
- CURRENT_MONTH_NAME
- CURRENT_MONTH_NAME_SHORT
- CURRENT_DATE
- CURRENT_DAY_NAME
- CURRENT_DAY_NAME_SHORT
- CURRENT_HOUR
- CURRENT_MINUTE
- CURRENT_SECOND
- CURRENT_SECONDS_UNIX
- BLOCK_COMMENT_START
- BLOCK_COMMENT_END
- LINE_COMMENT

Authors:
  Alexey Torgashin (CudaText)
  Oleh Lutsak (https://github.com/OlehL)
License: MIT

```</details>----------
   
   
Name: SnipToCall  
Description: Allows to use snippet-strings to call any commands (internal or plugins). Can be configured also from "Configure Hotkeys" plugin.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives the new way for calling commands (internal in CudaText, and external from plugins, e.g. ExtTools or Macros).

Adds one item to Plugins menu: "Configure SnipToCall".
Assign snip-strings to some commands, e.g. "pu" for "caret page up". Then you can type in any text "/pu" and press Tab. Snip-string will be removed, and assigned command will run. Between "/" and snip-string the number allowed, it is repeat-counter. So "/5pu" will do 5 page-ups.

Also plugin "Configure Hotkeys" is changed, in it you can also see and change snip-strings.

Author: A.Kvichanskiy (kvichans at github.com)

```</details>----------
   
   
Name: Spell Checker  
Description: Spell checker, based on Hunspell dictionaries. Shows red underlines for misspelled words, gives suggestions dialog.  
<details><summary>readme</summary>
```
Plugin for CudaText.
Gives spell checking by using Enchant/PyEnchant libraries.
Misspelled words are highlighted with red underlines.

- Windows 32-bit and 64-bit: supported, binary DLL files shipped with plugin
- Unix: supported, but you must install Enchant binary files (using OS package manager)

Uses Hunspell dictionaries.
It's possible to install additional dictionaries:
https://github.com/titoBouzout/Dictionaries
Rename to short names: Russian.* to ru.* or ru_RU.*
Copy into folder:
    - on Windows (32 bit CudaText): [CudaText_dir]\py\cuda_spell_checker\enchant_x86\share\enchant\myspell\
                 (64 bit CudaText): [CudaText_dir]\py\cuda_spell_checker\enchant_x64\share\enchant\myspell\
    - on Unix: ~/.enchant/myspell/

------------------------------

Use commands in "Plugins" menu:

    - "Check text", "Check text, with suggestions": Run spell-checking, and with suggestion-dialog for misspelled words. Dialog will give suggestions from spell-check engine.
    - "Check word", "Check word, with suggestions": Run spell-checking of only one word, under 1st caret.
    - "Go to next/previous misspelled": Put caret to next (previous) misspelled word, if such words are already highlighted.

Use commands in "Options / Settings-plugins / Spell Checker" menu:

    - "Select language": Shows menu-dialog to choose one of installed spelling dictionaries.

    - "Enable/disable checking on opening file": This toggles auto-checking after file opening, on/off.
      This writes option to install.inf file, in "py" folder. So you must re-enable this option
      after each plugin update/installation.

    - "Enable/disable checking after text editing": Enable/disable checking after every change of text,
      after 2 second pause (pause after last change of text, so you must stop typing the text and wait).
      This pause can be changed in CudaText config user.json. See option "py_change_slow".

Spell checker confirmation dialog buttons:
    - Ignore: skip word
    - Change: replace word in editor, from dialog input box or selected listbox item
    - Add: skip word and add it to a user dictionary for future
    - Cancel: stop all work

------------------------------

Feature:
For lexers, not entire text is checked, but only words in "syntax comments" and "syntax strings". For none-lexer, entire text is checked. To set which lexer styles are "comments" and "strings", open Lexer Properties dialog in CudaText, and use "Commenting" tab of dialog to set these styles. E.g. in HTML/Markdown lexers, correct styles are set, so correct parts are checked.

Feature:
You can enable permanent checking after a) file opening, b) text editing.
a) For file opening. Use API event "on_open", write it to file "py/cuda_spell_checker/install.inf" like this:
[item1]
section=events
events=on_open
b) For text editing. Use API event "on_change_slow", write it to the same install.inf file like this:
[item1]
section=events
events=on_change_slow
c) If both API events are needed, write them comma-separated:
[item1]
section=events
events=on_open,on_change_slow

Note: file install.inf is overwritten on each plugin update/installation.

------------------------------

Plugin have several options in ini-file, call command "Options / Settings-plugins / Spell Checker / Config".
Options:
    - "lang": current language which user chose in "Select language" command
    - "underline_style" (0..6): style of line below words
    - "confirm_esc_key" (0/1): allows to show confirmation when user presses Esc during long checking
    - "file_extension_list": which files to check with option "Enable checking after text editing":
        - "" (empty): disable on all files
        - "*": enable on all files
        - comma-separated list like "ext1,ext2,ext3": these extensions will be checked


Author: Alexey Torgashin (CudaText)
License: MIT

```</details>----------
   
   
Name: SPIR Helper  
Description: Auto-completion for SPIR lexer  
<details><summary>readme</summary>
```
plugin for CudaText.
provides auto-completion for SPIR (i.e. SPIR-V) lexer.

handles two kinds of completions:
- if caret is inside variable (starting with % char). here plugin suggests all possible variables from current file.
- if caret is inside SPIR keyword (for example, starting with "Op"). here plugin suggests possible keywords, from its local database in JSON format (official database for SPIR language).

authors:
  Artem Gavrilov, https://github.com/Artem3213212
  Alexey Torgashin (CudaText)
license: MIT

```</details>----------
   
   
Name: SQL Tools  
Description: Swiss army knife for your SQL databases. Gives lot of commands to work with databases: execute queries, format queries, show tables schema, show tables records, etc.  
<details><summary>readme</summary>
```
plugin for CudaText.
provides auto-completion for SPIR (i.e. SPIR-V) lexer.

handles two kinds of completions:
- if caret is inside variable (starting with % char). here plugin suggests all possible variables from current file.
- if caret is inside SPIR keyword (for example, starting with "Op"). here plugin suggests possible keywords, from its local database in JSON format (official database for SPIR language).

authors:
  Artem Gavrilov, https://github.com/Artem3213212
  Alexey Torgashin (CudaText)
license: MIT

```</details>----------
   
   
Name: Sum Lines  
Description: Calculates sum/min/max/avg of numbers in selected lines  
<details><summary>readme</summary>
```
Plugin for CudaText.
Plugin gives command "Sum Lines", which sums numbers in selection. 
Supported normal/column selections. 
Multi-selections not yet supported.

Empty/spaces lines are ignored.
Float numbers (with dot) are supported.
It shows report in a new tab.

Example of selected text:

    10
    100.10
    dd
    20.005
    100.10d

Report will be like:

    Normal selection: lines 10..14

    Sum: 130.105
    Min: 10.0
    Max: 100.1
    Avg: 43.36833333333333
    Numbers processed: 3
    Lines processed: 5
    Lines skipped: 2
      - selection line 3:     dd
      - selection line 5:     100.10d


Author: Alexey (CudaText)
License: MIT

```</details>----------
   
   
Name: Switch Header  
Description: Switches file pairs: c<>h, cpp<>h, cc<>h, asm<>inc  
<details><summary>readme</summary>
```
plugin for CudaText.
gives command to switch from the current file to its pair file, usually from source-code file to header-file (and vice versa). for example: 
*.cpp --> *.h or *.hpp (which is found)
*.h --> *.c or *.cpp (which is found)
*.asm --> *.inc

plugin has config file, which you can edit by menu item:
Options / Settings-plugins / Switch Header / Config

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: Sync Editing  
Description: Syncronized Editing like in SynWrite editor. Select block, activate plugin, and then you can rename equal identifiers in this block, by editing one identifier.  
<details><summary>readme</summary>
```
Plugin for CudaText
Sync Editing feature to edit identical identifiers, inspired by SynWrite editor.

Usage:
 - Select block (one or several lines), containing some ID's (identifiers)
 - Activate plugin by menu item: "Plugins / Sync Editing / Activate"
 - Selection is removed but plugin colorizes that block in different color
 - Click on any ID in that block, which you want to edit
 - Edit it (type new text)
 - To cancel Sync Editing: click somewhere else; or leave ID's line (e.g. with arrow keys); or call menu item "Plugins / Sync Editing / Cancel"

Plugin has several options, which are listed/described in the help message-box. 
Call menu item "Options / Settings-plugins / Sync Editing / Config".
Options "case sensitive", "reg.ex. for identifiers" and few UI options.

Plugin ignores IDs, which are located in syntax comments/strings.
To detect comments/strings, plugin uses lexer API, it wants words
with lexer style, beginning with "Id", but not containing "keyword".

Author: Vladislav Utkin (viad00 at GitHub)
License: MIT

```</details>----------
   
   
Name: Sync Scroll  
Description: Synchronizes vertical and/or horizontal scrolling of editors in groups 1 and 2  
<details><summary>readme</summary>
```
plugin for CudaText.
it sync's vertical and/or horizontal scrolling for active files in groups 1 and 2.
it gives 2 commands: "Sync vertical scroll", "Sync horizontal scroll".
it is function from Notepad++ and SynWrite editors.

plugin requires group-mode "2 horz" or "2 vert".
on changing group-mode to another, plugin deactivates.
plugin subscribes to editor event dinamically, so it don't slow down editor, if not active.

authors:
  Alexey Torgashin (CudaText)
  Artem Gavrilov (@Artem3213212 at GitHub)
license: MIT

```</details>----------
   
   
Name: Tab Colors  
Description: Allows to colorize tab headers per lexer, or per file extension  
<details><summary>readme</summary>
```
Plugin for CudaText.
Allows to colorize ui-tabs headers: per lexer, and per file extension.
Plugin has config file in JSON format, to open it, call
"Options / Settings-plugins / Tab Colors / Config" menu item.
Config has pairs "key":"value".

- "key": Lexer name, or just file extension with leading dot (it can be double extension too).
  Lexer name is compared case-insensitive here.
- "value": String with HTML color like "#rrggbb" or "#rgb".
  In the case of bad color string, plugin prints error to Console panel.

Authors:
  Alexey (CudaText)
  Shovel (CudaText forum user)
License: MIT

```</details>----------
   
   
Name: Tab Icons  
Description: Shows file-type icons on tab headers (same icons, which Project Manager shows)  
<details><summary>readme</summary>
```
plugin for CudaText.
it shows file-type-icons on UI tab headers. icons are loaded from themes, from subfolder
"data/filetypeicons". by default, preinstalled theme "vscode_16x16" is used, 
but you can use any other theme, after you install it in Addon Manager.
to set another theme, call menu item "Options / Settings-plugins / Tab Icons / Config",
in opened file plugins.ini find section [tab_icons], and change value of option there
to the name of subfolder in "data/filetypeicons".

for themes with bigger icon size (e.g. 24x24) you will need to adjust CudaText option
"ui_tab_size_y", to make UI tabs height bigger.

author: Alexey (CudaText)
license: MIT

```</details>----------
   
   
Name: Terminal  
Description: Gives "Terminal" panel in the bottom panel of CudaText  
<details><summary>readme</summary>
```
Plugin for CudaText.
Adds panel "Terminal" to the bottom panel of CudaText. It is emulation of terminal (default: Bash on Unix, Cmd on Windows). You can enter commands in this terminal, and see output from shell. 
Limitation: don't use interactive commands, which need keyboard input.

Plugin has several options in the .ini file, call menu item:
"Options / Settings-plugins / Terminal / Config".

Hotkeys in the terminal:
- Ctrl+Down: show last commands menu, insert chosen item to input field
- Up, Down arrows: scroll the memo area
- Esc: close terminal and focus editor
- Break: interrupt/restart shell process

Authors:
- Alexey Torgashin (CudaText)
- Artem Gavrilov https://github.com/Artem3213212

License: MIT
Credits for icon: GitHub.com, MIT license

```</details>----------
   
   
Name: Testing of Code Tree API  
Description: Plugin tests filling Code Tree by API: for Markdown lexer, it fills Code Tree with some fake lines  
<details><summary>readme</summary>
```
Plugin for CudaText.
Adds panel "Terminal" to the bottom panel of CudaText. It is emulation of terminal (default: Bash on Unix, Cmd on Windows). You can enter commands in this terminal, and see output from shell. 
Limitation: don't use interactive commands, which need keyboard input.

Plugin has several options in the .ini file, call menu item:
"Options / Settings-plugins / Terminal / Config".

Hotkeys in the terminal:
- Ctrl+Down: show last commands menu, insert chosen item to input field
- Up, Down arrows: scroll the memo area
- Esc: close terminal and focus editor
- Break: interrupt/restart shell process

Authors:
- Alexey Torgashin (CudaText)
- Artem Gavrilov https://github.com/Artem3213212

License: MIT
Credits for icon: GitHub.com, MIT license

```</details>----------
   
   
Name: Testing of dialog API  
Description: Testing plugin of CudaText dialog API  
<details><summary>readme</summary>
```
Plugin for CudaText.
Adds panel "Terminal" to the bottom panel of CudaText. It is emulation of terminal (default: Bash on Unix, Cmd on Windows). You can enter commands in this terminal, and see output from shell. 
Limitation: don't use interactive commands, which need keyboard input.

Plugin has several options in the .ini file, call menu item:
"Options / Settings-plugins / Terminal / Config".

Hotkeys in the terminal:
- Ctrl+Down: show last commands menu, insert chosen item to input field
- Up, Down arrows: scroll the memo area
- Esc: close terminal and focus editor
- Break: interrupt/restart shell process

Authors:
- Alexey Torgashin (CudaText)
- Artem Gavrilov https://github.com/Artem3213212

License: MIT
Credits for icon: GitHub.com, MIT license

```</details>----------
   
   
Name: Testing of gaps API  
Description: Plugin to test CudaText Editor.gaps() API  
<details><summary>readme</summary>
```
Plugin for CudaText.
Adds panel "Terminal" to the bottom panel of CudaText. It is emulation of terminal (default: Bash on Unix, Cmd on Windows). You can enter commands in this terminal, and see output from shell. 
Limitation: don't use interactive commands, which need keyboard input.

Plugin has several options in the .ini file, call menu item:
"Options / Settings-plugins / Terminal / Config".

Hotkeys in the terminal:
- Ctrl+Down: show last commands menu, insert chosen item to input field
- Up, Down arrows: scroll the memo area
- Esc: close terminal and focus editor
- Break: interrupt/restart shell process

Authors:
- Alexey Torgashin (CudaText)
- Artem Gavrilov https://github.com/Artem3213212

License: MIT
Credits for icon: GitHub.com, MIT license

```</details>----------
   
   
Name: Text Statistics  
Description: Shows for current text: count of lines, words, letters, all chars  
<details><summary>readme</summary>
```
plugin for CudaText.
gets statistics for text in the current editor tab.
and shows it in a message-box, also allowing to output report to a new file.
gets info:

- count of lines/ all chars/ letter chars
- count of words (with alpha-numerical chars)
- most common words (up to 30, can change this number in source code)
- count of sentences which have n (1 to 9) words
- additional command: find all sentences, and output them to a new tab
 

author: Alexey T.
license: MIT

```</details>----------
   
   
Name: Textile Preview  
Description: Previews Textile documents as HTML page in browser  
<details><summary>readme</summary>
```
Plugin for CudaText.
It converts Textile text to HTML (using Python Textile library), and then opens HTML file in browser. 


Author: Alexey T.
License: MIT

```</details>----------
   
   
Name: TextToSpeech  
Description: Speak text using Windows Speech API  
<details><summary>readme</summary>
```
Plugin for CudaText.
Uses system-provided speech synthesis platform to speak text.
Windows only (yet), the "SAPI" speech engine/platform is used.
Requires additional package "pywin32", from CudaText addons.

Speaks selected text, or entire document if nothing selected.

Plugin has config file, to call it: "Options / Settings-plugins / TextToSpeech".
Option "tts_voice" allows to change voice, e.g. to "Microsoft Sam" or "Microsoft David".

Ported from Sublime Text plugin "TextToSpeech".
Author: Alexey Torgashin (CudaText)
License: MIT

```</details>----------
   
   
Name: Vim Mode  
Description: Allows to use Vim key bindings  
<details><summary>readme</summary>
```
plugin for CudaText.
command in Plugins menu activates Vim key bindings, initially in Vim command mode. Vim mode is activated in all editor tabs at once. 

indication of modes:
- Vim command mode: full-block-frame caret
- Vim visual mode: half-block caret
- Vim insertion mode: no indication, usual caret
 

a) Vim insertion mode - all keys work like usual in CudaText, only Esc goes to command mode
b) Vim replace mode - like insertion mode, but "insert/overwrite mode" is "overwrite"
c) Vim visual mode - all movement keys (arrows/home/end/pageup/pagedown) make selection w/o Shift
d) Vim command mode supported keys:

  h, j, k, l - move caret (4 arrows)

  w - go to next word (jumps not exactly like Vim, but like CudaText command "go to next word")
  W - currently the same as 'w'
  b - go to previous word (same note)
  B - currently the same as 'b'
  e - go to end of word (or next word)
  E - currently the same as 'e'

  a - enter insertion mode, after moving caret right
  A - enter insertion mode, at line end
  i - enter insertion mode, at current pos
  I - enter insertion mode, at first non-space char in line
  
  r - replace current char with next typed char, return to command mode
  R - enter replace mode

  o - creates empty line below, goes into insertion mode on new line
  O - creates empty line above, goes into insertion mode on new line

  gg - go to text begin
  G - go to line number (if number entered before), or go to text end (if none)

  | - go to column number (if number entered before, else column 1)
  0 - go to line begin (column 1)
  ^ - go to first non-whitespace
  - - go to first non-whitespace, in previous line
  + - go to first non-whitespace, in next line
  $ - go to line end

  x - delete char right (like Delete key)
  X - delete char left (like Backspace key)
  
  y - yank (copy) to clipboard
  Y - yank entire line
  p - paste from clipboard, after caret
  P - paste from clipboard, before caret
  d - cut to clipboard (only if text selected, else it's prefix)

  D - delete to end of line
  dd - delete current line
  db - delete to word begin
  dw, de - delete to word end (currently commands work the same)
  dL - delete to text end
  d/ - delete until position of text, which is asked in dialog
  df - delete until position of char entered after
  dt - delete until position of char entered after, minus one char
  dF - backward version of 'df'
  dT - backward version of 'dt'

  C - change to end of line (delete to end of line, go to insertion mode)
  c - change - like "d" commands (cd, cb, cw, ce...) but also goes to insertion mode 
  
  v - enter visual mode
  V - enter visual mode, but select entire lines
  
  Space - move right
  Backspace - move left
  
  / - search forward, prompts for string in dialog
  ? - search backward
  n - repeat search in the same direction
  N - repeat search in the opposite direction
  f - find next typed character, inside line
  F - backward version of "f"
  t - like "f" but set position minus one char
  T - backward version of "t"  

  u - undo
  ~ - invert case of selection (if selection) or one char
  # - go to next occurence of current word (looping from begin)
  . - repeat last command (entered in command mode)
  
  H - go to top line on screen
  M - go to middle line on screen
  L - go to bottom line on screen

  J - join current line with the next one
  S - substitute line - delete line, go to insertion mode
    
  zz - center the caret's line on screen
  z. - center the caret's line on screen, caret on first non-blank char
  zt - scroll the screen so the caret is at the top
  zb - scroll the screen so the caret is at the bottom

  ZZ - save current file, quit
  ZQ - quit without saving current file

  Ctrl+[  - the same as Esc key (removes multi-carets and returns from insertion mode to command mode)
  Ctrl+I  - the same as Tab key
  Ctrl+M  - the same as Enter key
  Ctrl+H  - the same as Backspace key


author: Alexey (CudaText)
suggestions/testing: @mangobait, @oO0XX0Oo, @acicovic
license: MIT

```</details>----------