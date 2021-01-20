# CudaText Plugins List (WIP)
<details><summary>How to install</summary>  
  Copy plugin directory to <code>py</code> directory that lives:
  
  * on portable version - alongside CudaText executable.      
  * on non-portable:
      * Linux, *BSD, Solaris: in ~/.config/cudatext, or $XDG_CONFIG_HOME/cudatext if this OS variable is set
      * macOS: in ~/Library/Application Support/CudaText
</details>  
  
  
TODO:  
* ~~fix formatting~~
* ~~add list ordered by popularity~~ (Medals on top plugins instead)
* ~~table of contents~~
---


* [Major](#major)  
* [Misc](#misc)  
* [Lexer-Specific](#lexer-specific)  
* [Editor Config](#editor-config)  
* [Extra](#extra)  
* [System](#system)  
* [Plugin/Dev](#plugindev)  

  
---
* ## Major
   
   
    * [Complete From Text](https://github.com/CudaText-addons/cuda_complete_from_text) [🥇](a "Top Downloaded") - Handles auto-completion command (Ctrl+Space) and gives list of words from the current document (or all documents, by option), starting from the currently typed word.      
   
   
    * [CudaExt](https://github.com/kvichans/cuda_ext) [🥇](a "Top Downloaded") - Additional commands for CudaText in Commands dialog and Plugins menu      
   
   
    * [CudaExt_py35](https://github.com/kvichans/cuda_ext) - Additional commands for CudaText in Commands dialog and Plugins menu (Python 3.5)      
   
   
    * [CudaLint](https://github.com/CudaText-addons/cuda_lint) [🥇](a "Top Downloaded") - Linting (syntax-checking) of source code. Needs "linters" for each lexer you want to check. See useful help in readme folder.      
   
   
    * [DevDocs](https://github.com/CudaText-addons/cuda_devdocs) [🥇](a "Top Downloaded") - Performs search on DevDocs site      
   
   
    * [Differ](https://github.com/OlehL/cuda_differ) [🥇](a "Top Downloaded") - Plugin to compare two files and show compare results side by side      
   
   
    * [ExtTools](https://github.com/kvichans/cuda_exttools) [🥇](a "Top Downloaded") - Adds support for calling external programs in CudaText      
   
   
    * [Favorites](https://github.com/kvichans/cuda_favorites) - Manages "favorites": list of user-selected file names, to quickly open them      
   
   
    * [Find in Files](https://github.com/kvichans/cuda_find_in_files) - Gives dialog to search for multiple files containing some string/regex, like in file managers.      
   
   
    * [Find in Files 4](https://github.com/kvichans/cuda_find_in_files4) [🥇](a "Top Downloaded") - Gives dialog to search for multiple files containing some string/regex, like in file managers.      
   
   
    * [Find in Files 4](https://github.com/kvichans/cuda_find_in_files4) [🥇](a "Top Downloaded") - Gives dialog to search for multiple files containing some string/regex, like in file managers.      
   
   
    * [Highlight Occurrences](https://github.com/CudaText-addons/cuda_hilite_occurrences) [🥇](a "Top Downloaded") - Highlights/Marks all occurrences of current/selected word/fragment      
   
   
    * [In-text complete](https://github.com/kvichans/cuda_intext_complete) - Suggests completions for syntax expressions, using fragments from the entire text      
   
   
    * [Macros](https://github.com/kvichans/cuda_macros) [🥇](a "Top Downloaded") - Macros manager for CudaText. Gives commands to record/playback/save/delete/etc macros.      
   
   
    * [Snippets](https://github.com/CudaText-addons/cuda_snippets) [🥇](a "Top Downloaded") - Snippets engine, described in CudaText wiki. Snippets are expanded by Tab-key or can be called from menu.      
   
   
    * [Sync Editing](https://github.com/viad00/cuda_sync_editing) [🥇](a "Top Downloaded") - Syncronized Editing like in SynWrite editor. Select block, activate plugin, and then you can rename equal identifiers in this block, by editing one identifier.      
   
   
    * [Terminal](https://github.com/Artem3213212/cuda_terminal) [🥇](a "Top Downloaded") - Gives "Terminal" panel in the bottom panel of CudaText      
   
   
* ## Misc
   
   
    * [Auto Center Line](https://github.com/CudaText-addons/cuda_auto_center_line) [🥇](a "Top Downloaded") - Plugin keeps current line in the center of the editor window      
   
   
    * [Auto-Copy to Clipboard](https://github.com/CudaText-addons/cuda_auto_copy) [🥇](a "Top Downloaded") - When text block selected, it's auto copied to clipboard, no need to press Ctrl+C (or call menu item). Don't work with multi-carets. Don't work for huge blocks (>50K).      
   
   
    * [Auto Replace](https://github.com/iRamSoft/cuda_auto_replace) [🥇](a "Top Downloaded") - Plugin auto-replaces currently typed words, based on set of snippets with such words.      
   
   
    * [Auto Save](https://github.com/CudaText-addons/cuda_auto_save) [🥇](a "Top Downloaded") - Saves modified files automatically: before file closing (by option, default is off), by timer (default interval 30sec), on application deactivation      
   
   
    * [Backup File](https://github.com/kvichans/cuda_backup_file) - Creates backup copy of current file, a) by command in Plugins, b) auto-creation before file saving      
   
   
    * [Calc Expression](https://github.com/CudaText-addons/cuda_calc_expr) - Gets selected math expression, e.g. "2.4 * sin(pi/3)", calculates it, replaces selection with result      
   
   
    * [Caret History](https://github.com/kvichans/cuda_caret_history) - Tracks caret pos changing (only long jumps), and allows to jump backward/forward by that history      
   
   
    * [Case Converter](https://github.com/CudaText-addons/cuda_case_converter) - Converts identifiers between several cases (snake_case, camelCase, PascalCase etc)      
   
   
    * [Color Picker](https://github.com/CudaText-addons/cuda_color_picker) [🥇](a "Top Downloaded") - Shows color-picker dialog, inserts color #rrggbb      
   
   
    * [Color Text](https://github.com/iRamSoft/cuda_color_text/) [🥇](a "Top Downloaded") - Allows to colorize text fragments, like function "Style token" in Notepad++      
   
   
    * [Colored Indent](https://github.com/CudaText-addons/cuda_colored_indent) [🥇](a "Top Downloaded") - Colorizes spaces/tabs in indents      
   
   
    * [Column Marks](https://github.com/CudaText-addons/cuda_column_marks) - Commands to work with additional margins (options "margin", "margin_string")      
   
   
    * [CudaFormatter](https://github.com/CudaText-addons/cuda_fmt) [🥇](a "Top Downloaded") - Framework to use code formatters as 2nd-level plugins      
   
   
    * [Detect Indent](https://github.com/CudaText-addons/cuda_detect_indent) [🥇](a "Top Downloaded") - Detects indentation (spaces or tabs, tab size) for opened files      
   
   
    * [EditorConfig Support](https://github.com/CudaText-addons/cuda_editorconfig) [🥇](a "Top Downloaded") - Supports EditorConfig system      
   
   
    * [Edits Navigation](https://github.com/halfbrained/cuda_edits_navigation) - Return to previously edited lines      
   
   
    * [Encode](https://github.com/cudatext-addons/cuda_encode) [🥇](a "Top Downloaded") - Allows to encode text using many transformations (Base64, URL escape, HTML/XML escape, Hash, etc)      
   
   
    * [Extended Selection](https://github.com/halfbrained/cuda_extended_selection) [🥇](a "Top Downloaded") - Extend double/triple-click selection while holding Shift      
   
   
    * [Extract Strings](https://github.com/CudaText-addons/cuda_extract_strings) - Shows dialog to enter RegEx, this RegEx will find list of strings. You can choose what to do with these strings: copy to clipboard, copy to new tab. Also includes Filter Lines command to find lines.      
   
   
    * [File Type Profile](https://github.com/dinkumoil/cuda_file_type_profile) - Create profiles for files with certain filename extensions and apply the settings automatically when opening a file.      
   
   
    * [file URI handler](https://github.com/halfbrained/cuda_file_uri_handler) - Opens file:/// links in CudaText      
   
   
    * [Focus Mode](https://github.com/CudaText-addons/cuda_focus_mode) - Shades/dims all lines except the current paragraph. Plugin is active only for some lexers, call "Plugins/ Focus Mode/ Config".      
   
   
    * [Git Status](https://github.com/CudaText-addons/cuda_git_status) - Shows Git information in statusbar: current branch name, clean state, etc.      
   
   
    * [Hash Generator](https://github.com/CudaText-addons/cuda_hash_gen) [🥇](a "Top Downloaded") - Dialog which allows to calculate hash sums (several algorithms) for files/strings      
   
   
    * [Hex Dump](https://github.com/CudaText-addons/cuda_hex_dump) [🥇](a "Top Downloaded") - Shows text in hex-dump format      
   
   
    * [Highlight Variables](https://github.com/CudaText-addons/cuda_hilite_vars) - Highlights "variables" inside strings literals (for Bash lexer, etc)      
   
   
    * [IP Address Helper](https://github.com/medvosa/cuda_ip_address_helper) - When mouse hovers IP address in text, plugin shows country of that address in the statusbar      
   
   
    * [Insert Pics](https://github.com/CudaText-addons/cuda_insert_pics) - Allows to insert preview of pictures (png/jpeg/gif/bmp/ico) into text. Saves pictures in helper file, to automatically load pics on file re-opening.      
   
   
    * [In-text bookmarks](https://github.com/kvichans/cuda_intext_bookmarks) - Allows to place bookmarks as text-comments (permanent bookmarks), and to navigate to them      
   
   
    * [Micro Utils](https://github.com/CudaText-addons/cuda_micro_utils) - Minor commands to work with bin/hex numbers, etc      
   
   
    * [Numbered Bookmarks](https://github.com/CudaText-addons/cuda_numbered_bookmarks) [🥇](a "Top Downloaded") - Allows to set and go to numbered bookmarks (1..8)      
   
   
    * [Online Search](http://github.com/cudatext-addons/cuda_online_search) [🥇](a "Top Downloaded") - Opens webbrowser with search for selection/word, supports several search engines      
   
   
    * [Open URL](https://github.com/CudaText-addons/cuda_open_url) [🥇](a "Top Downloaded") - Gives commands to open URL (under text caret) in many browsers      
   
   
    * [Paste as String](https://github.com/CudaText-addons/cuda_paste_as_string) - Pastes text from Clipboard as "string" for current lexer      
   
   
    * [Plain Tasks](https://github.com/OlehL/cuda_plain_tasks) - ToDo-list plugin for CudaText      
   
   
    * [SnipToCall](https://github.com/kvichans/cuda_snip_to_call) - Allows to use snippet-strings to call any commands (internal or plugins). Can be configured also from "Configure Hotkeys" plugin.      
   
   
    * [Spell Checker](https://github.com/CudaText-addons/cuda_spell_checker) [🥇](a "Top Downloaded") - Spell checker, based on Hunspell dictionaries. Shows red underlines for misspelled words, gives suggestions dialog.      
   
   
    * [Sync Scroll](https://github.com/Artem3213212/cuda_sync_scroll) [🥇](a "Top Downloaded") - Synchronizes vertical and/or horizontal scrolling of editors in groups 1 and 2      
   
   
    * [TextToSpeech](https://github.com/CudaText-addons/cuda_texttospeech) - Speak text using Windows Speech API      
   
   
    * [Tab Colors](https://github.com/CudaText-addons/cuda_tab_colors) [🥇](a "Top Downloaded") - Allows to colorize tab headers per lexer, or per file extension      
   
   
    * [Tab Icons](https://github.com/CudaText-addons/cuda_tab_icons) [🥇](a "Top Downloaded") - Shows file-type icons on tab headers (same icons, which Project Manager shows)      
   
   
    * [Vim Mode](https://github.com/CudaText-addons/cuda_vim_mode) [🥇](a "Top Downloaded") - Allows to use Vim key bindings      
   
   
* ## Lexer-Specific
   
   
    * [AutoIt Helper](https://github.com/OlehL/cuda_autoit_helper) - Autocompletion and function hints for AutoIt Lexer      
   
   
    * [CSS CanIUse](https://github.com/CudaText-addons/cuda_css_caniuse) [🥇](a "Top Downloaded") - For CSS files, shows info about selected word from CanIUse.com site      
   
   
    * [CSS Inspector](https://github.com/cudatext-addons/cuda_css_inspector) - Plugin shows in HTML document CSS properties of current tag      
   
   
    * [CSS Property Info](https://github.com/medvosa/cuda_css_property_info) - Shows information about selected CSS property in statusbar      
   
   
    * [CSS Table of Contents](https://github.com/CudaText-addons/cuda_css_toc) - For CSS files: creates table-of-contents, its sections/sub-sections      
   
   
    * [FontStorage](https://github.com/CudaText-addons/cuda_webfont) - In CSS code, inserts usage of external fonts from FontStorage.com site      
   
   
    * [CSV Helper](https://github.com/Artem3213212/cuda_csv_hilite) [🥇](a "Top Downloaded") - Highlights columns in CSV and TSV files with different colors. Gives several commands to manage columns. Requires "CSV" and "TSV" lite lexers installed.      
   
   
    * [DocBlock](https://github.com/CudaText-addons/cuda_docblock_comments) [🥇](a "Top Downloaded") - Helps to type DocBlock comments, for JS/PHP lexers      
   
   
    * [Emmet Lite](https://github.com/CudaText-addons/cuda_emmet_lite) - Emmet engine, see www.emmet.io      
   
   
    * [Fountain Helper](https://github.com/CudaText-addons/cuda_fountain_helper) - Helper for Fountain lexer: 1) On Shift+Enter it converts line to upper-case and makes new-line, 2) Command to list dialogs of some character, 3) Command to list all scenes, 4) Command to extract all dialogs of some character, 5) On Ctrl+Space after partial character name it gives auto-completion list, 6) Preview as HTML in browser.      
   
   
    * [HTML Completion](https://github.com/Artem3213212/cuda_html_completion) - Handles auto-completion (Ctrl+Space) in HTML/PHP files. 1) Auto-completion with file names, when caret is inside IMG tag. 2) Auto-completion with CSS class/id names, when caret is inside 'class=""' or 'id=""'.      
   
   
    * [HTML Live Preview](https://github.com/medvosa/cuda_html_live_preview) - Provides live preview for HTML files with support of dynamically linked sources      
   
   
    * [HTML Ops](https://github.com/cudatext-addons/cuda_html_ops) - Commands to work with HTML/CSS      
   
   
    * [HTML Tooltips](https://github.com/CudaText-addons/cuda_html_tooltips) [🥇](a "Top Downloaded") - In HTML/CSS files, plugin shows tooltips for: HTML color values, HTML entities, picture filenames      
   
   
    * [HTML Tidy](https://github.com/CudaText-addons/cuda_html_tidy) [🥇](a "Top Downloaded") - Validates HTML documents using Tidy tool      
   
   
    * [JS Multiline Array](https://github.com/CudaText-addons/cuda_js_multiline_array) - Converts several selected lines of text - to JavaScript string array      
   
   
    * [JS Tern](https://github.com/pohmelie/cuda_tern) - Gives intelligence commands for JavaScript: 1) auto-complete (Ctrl+Space), 2) go-to-definition (item in context menu), 3) show function call-tip, 4) show doc-string, 5) show usages. Based on Tern engine, requires Node.js.      
   
   
    * [Markdown Editing](https://github.com/CudaText-addons/cuda_markdown_editing) [🥇](a "Top Downloaded") - Helpers for editing Markdown documents      
   
   
    * [Markdown Preview](https://github.com/CudaText-addons/cuda_markdown_preview) [🥇](a "Top Downloaded") - Previews Markdown text as HTML page in browser      
   
   
    * [Pandoc Helper](https://github.com/CudaText-addons/cuda_pandoc) - Uses Pandoc tool, to convert several markup formats to output formats, which Pandoc supports (Word, PDF, Markdown etc)      
   
   
    * [Configure PyCodeStyle linter](https://github.com/kvichans/cuda_config_pep8) - Shows dialog to configure PyCodeStyle linter, and save its config      
   
   
    * [Python IntelliSense](https://github.com/CudaText-addons/cuda_python_intel) [🥇](a "Top Downloaded") - Supports intelligence commands for Python: 1) auto-completion (Ctrl+Space), 2) goto-definition (item in context menu), 3) show function call-tip (Ctrl+Shift+Space), 4) show function doc-string, 5) show usages of name. Based on Jedi library.      
   
   
    * [SPIR Helper](https://github.com/Artem3213212/cuda_spir_helper) - Auto-completion for SPIR lexer      
   
   
    * [SQL Tools](https://github.com/mtxr/CudaText-SQLTools) - Swiss army knife for your SQL databases. Gives lot of commands to work with databases: execute queries, format queries, show tables schema, show tables records, etc.      
   
   
    * [Textile Preview](https://github.com/CudaText-addons/cuda_textile_preview) - Previews Textile documents as HTML page in browser      
   
   
    * [reStructuredText Preview](https://github.com/CudaText-addons/cuda_rest_preview) - Previews reStructuredText file as HTML page in browser      
   
   
* ## Editor Config
   
   
    * [Config Toolbar](https://github.com/CudaText-addons/cuda_config_toolbar) [🥇](a "Top Downloaded") - Configures main toolbar in CudaText: icon-set and buttons      
   
   
    * [Configure Hotkeys](https://github.com/kvichans/cuda_config_keys) - Shows dialog to view/set hotkeys in editor      
   
   
    * [Config Menu](https://github.com/kvichans/cuda_config_menu) - Allows to customize CudaText top/context menus, using JSON files      
   
   
    * [Session Manager](https://github.com/kvichans/cuda_sess_manager) - Allows to manage "sessions" in editor      
   
   
* ## Extra
   
   
    * [ASCII Art](https://github.com/CudaText-addons/cuda_ascii_art) - Inserts text formatted via ASCII art font (using PyFiglet)      
   
   
    * [Draw Lines](https://github.com/CudaText-addons/cuda_draw_lines) [🥇](a "Top Downloaded") - Draws pseudo-graphic frames in text, by Shift+arrows      
   
   
    * [Insert Emoji](https://github.com/CudaText-addons/cuda_insert_emoji) - Dialog with list of most common emojis (about 900), to insert emoji name like :smile:      
   
   
    * [Lorem Ipsum](https://github.com/CudaText-addons/cuda_lorem_ipsum) - Inserts "Lorem Ipsum" text (placeholder for HTML pages)      
   
   
    * [Number Utils](https://github.com/CudaText-addons/cuda_number_utils) [🥇](a "Top Downloaded") - Commands for numbers: insert row of numbers, convert to text or Romans, etc.      
   
   
    * [Options Report](https://github.com/kvichans/cuda_opts_report) - Shows HTML page with report of options      
   
   
    * [Password Generator](https://github.com/ildarkhasanshin/cuda_pass_gen) - Generating a random password of a certain length from certain characters      
   
   
    * [Remove Greek Accents](https://github.com/CudaText-addons/cuda_remove_greek_accents) - Replaces Greek letters with accents - to similar letters without accents      
   
   
    * [Show Unicode Name](https://github.com/CudaText-addons/cuda_show_unicode_name) - Shows full Unicode name of a character under first caret, in the statusbar      
   
   
    * [Switch Header](https://github.com/CudaText-addons/cuda_switch_header) - Switches file pairs: c<>h, cpp<>h, cc<>h, asm<>inc      
   
   
    * [Text Statistics](https://github.com/CudaText-addons/cuda_text_statistics) [🥇](a "Top Downloaded") - Shows for current text: count of lines, words, letters, all chars      
   
   
    * [Sum Lines](https://github.com/CudaText-addons/cuda_sum_lines) - Calculates sum/min/max/avg of numbers in selected lines      
   
   
* ## System
   
   
    * [Explorer Integration](https://github.com/CudaText-addons/cuda_explorer_integration) - For Windows: allows to add/remove Explorer context menu item for CudaText, to associate CudaText with file-extensions .txt .ini .cuda-proj .cuda-session.      
   
   
    * [FTP](https://github.com/pohmelie/cuda_ftp) [🥇](a "Top Downloaded") - Allows to handle remote files/folders on FTP+SFTP servers. Read text file about SFTP support.      
   
   
    * [Fonts](https://github.com/CudaText-addons/cuda_fonts) - Allows to use portable fonts only in CudaText. Fonts are loaded from CudaText data/fonts folder.      
   
   
    * [NTFS Streams](https://github.com/CudaText-addons/cuda_ntfs_streams) - Allows to work with NTFS file streams (Windows)      
   
   
    * [SFTP support for FTP plugin, Windows x32/x64, Python 3.5](https://github.com/CudaText-addons/cuda_ftp_libs_py35)    
   
   
    * [SFTP support for FTP plugin, Windows x32/x64, Python 3.6](https://github.com/CudaText-addons/cuda_ftp_libs_py36)    
   
   
    * [SFTP support for FTP plugin, Windows x32/x64, Python 3.7](https://github.com/CudaText-addons/cuda_ftp_libs_py37)    
   
   
    * [pywin32 libraries](https://github.com/CudaText-addons/cuda_pywin32)    
   
   
* ## Plugin/Dev
   
   
* ## ?
   
   
    * [Dash Help](http://github.com/cudatext-addons/cuda_dash_help) - Opens Dash help pages, for selected text or current word      
   
   
    * [Font Awesome](https://github.com/TomBraider42/cuda_fontawesome) - Search FontAwesome Icons in sidebar and insert the codes in editor.      