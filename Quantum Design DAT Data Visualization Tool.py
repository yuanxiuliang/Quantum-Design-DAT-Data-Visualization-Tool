from tkinter import ttk, filedialog, messagebox
import tkinter as tk
import os
import platform
import ctypes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import matplotlib as mpl
import locale

# 多语言支持
def detect_system_language():
    """检测系统语言，返回 'zh' 或 'en'"""
    try:
        # 获取系统语言设置
        system_lang = locale.getdefaultlocale()[0]
        if system_lang and system_lang.startswith('zh'):
            return 'zh'
        else:
            return 'en'
    except:
        return 'en'

def get_texts(lang=None):
    """获取指定语言的文本字典"""
    if lang is None:
        lang = detect_system_language()
    
    texts = {
        'zh': {
            'app_title': 'Quantum Design 的 DAT 数据透视工具',
            'file_info': '文件信息',
            'no_file': '未加载文件',
            'total_points': '总数据点数',
            'coord_selection': '坐标选择',
            'data_filter': '数据筛选',
            'filter_col': '筛选列',
            'filter_mean': '筛选均值',
            'tolerance': '容差',
            'min_length': '最小连续行数',
            'filter_btn': '筛选',
            'plot_range': '绘图范围',
            'start_row': '起始行',
            'end_row': '终止行',
            'plot_type': '绘图类型',
            'line_plot': '折线',
            'scatter_plot': '散点',
            'both_plot': '折线+散点',
            'open_file': '打开 .dat',
            'copyright': '版权所有者： 袁 秀良, 联系邮件：yuanxiuliang8@outlook.com, 项目地址: https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool',
            'status_ready': '就绪',
            'status_file_loaded': '文件已加载',
            'status_plot_drawn': '绘图完成',
            'status_zoom_applied': '已放大到区域',
            'status_no_zoom_history': '没有可回退的缩放历史',
            'error_file_format': '文件格式错误',
            'error_no_data': '未找到数据段',
            'error_column_not_found': '列不存在',
            'progress_loading': '正在加载文件...',
            'progress_processing': '正在处理数据...',
        },
        'en': {
            'app_title': 'Quantum Design DAT Data Visualization Tool',
            'file_info': 'File Information',
            'no_file': 'No file loaded',
            'total_points': 'Total data points',
            'coord_selection': 'Coordinate Selection',
            'data_filter': 'Data Filtering',
            'filter_col': 'Filter Column',
            'filter_mean': 'Mean',
            'tolerance': 'Tolerance',
            'min_length': 'Min Continuous Rows',
            'filter_btn': 'Filt',
            'plot_range': 'Plot Range',
            'start_row': 'Start Row',
            'end_row': 'End Row',
            'plot_type': 'Plot Type',
            'line_plot': 'Line',
            'scatter_plot': 'Scatter',
            'both_plot': 'Line+Scatter',
            'open_file': 'Open .dat',
            'copyright': 'Copyright: Yuan Xiuliang, Email: yuanxiuliang8@outlook.com, Project: https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool',
            'status_ready': 'Ready',
            'status_file_loaded': 'File loaded',
            'status_plot_drawn': 'Plot completed',
            'status_zoom_applied': 'Zoomed to region',
            'status_no_zoom_history': 'No zoom history to go back',
            'error_file_format': 'Invalid file format',
            'error_no_data': 'No data section found',
            'error_column_not_found': 'Column not found',
            'progress_loading': 'Loading file...',
            'progress_processing': 'Processing data...',
        }
    }
    return texts[lang]

def set_dpi_awareness():
    """Enable DPI awareness on Windows so UI scales correctly on high-DPI screens."""
    if platform.system() != "Windows":
        return
    # Try modern API first, then fall back.
    try:
        # PROCESS_PER_MONITOR_DPI_AWARE = 2
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

def get_system_dpi():
    """Return system DPI (pixels per inch). Default 96 if unavailable."""
    dpi = 96
    if platform.system() == "Windows":
        try:
            # ensure we can query DPI
            user32 = ctypes.windll.user32
            user32.SetProcessDPIAware()
            hdc = user32.GetDC(0)
            LOGPIXELSX = 88
            dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, LOGPIXELSX)
        except Exception:
            pass
    return dpi

class DatPlotterApp:
    def __init__(self, root, dpi=96, scaling=1.0):
        
        # 初始化多语言支持
        self.texts = get_texts()
        
        # allow non-GUI usage in tests by passing root=None
        if root is None:
            # minimal attributes required for non-GUI operations/tests
            self.root = None
            self.filepath = None
            self.df = None
            self.fileopentime_ts = None
            self.fileopentime_dt = None
            self.dpi = dpi
            self.scaling = scaling
            # minimal non-GUI placeholders
            self._preview_patch = None
            self.plot_type_var = None
            self.convert_time_var = None
            # other GUI attributes left uninitialized when root is None
            return
        
        self.root = root
        self.root.title(self.texts['app_title'])
        self.filepath = None
        self.df = None
        self.fileopentime_ts = None
        self.fileopentime_dt = None
        self.dpi = dpi
        self.scaling = scaling
        # GUI state vars
        self._preview_patch = None
        self.plot_type_var = tk.StringVar(value="both")
        # overlay state: mapping tree-iid -> list of matplotlib artists
        self._overlay_artists = {}
        self._max_overlays = 8
        self.convert_time_var = tk.BooleanVar(value=False)
        
        # zoom functionality
        self._zoom_stack = []  # stack of (xlim, ylim) tuples for zoom history
        self._is_selecting = False
        self._select_start = None
        self._select_end = None
        self._selection_rect = None

        # adjust matplotlib global sizes to suit high-DPI
        try:
            mpl.rcParams['figure.dpi'] = self.dpi
            mpl.rcParams['savefig.dpi'] = self.dpi
            mpl.rcParams['axes.titlesize'] = max(10, mpl.rcParams.get('axes.titlesize', 12) * self.scaling)
            mpl.rcParams['axes.labelsize'] = max(9, mpl.rcParams.get('axes.labelsize', 10) * self.scaling)
            mpl.rcParams['xtick.labelsize'] = max(8, mpl.rcParams.get('xtick.labelsize', 8) * self.scaling)
            mpl.rcParams['ytick.labelsize'] = max(8, mpl.rcParams.get('ytick.labelsize', 8) * self.scaling)
            mpl.rcParams['legend.fontsize'] = max(8, mpl.rcParams.get('legend.fontsize', 9) * self.scaling)
        except Exception:
            pass
        
        # 设置UI字体大小为140%
        self.ui_font_size = int(9 * 1.4)  # 基础字体大小9，放大到140%
        self.ui_font = ("Microsoft YaHei", self.ui_font_size)  # 使用微软雅黑字体
        
        # 配置自定义样式
        self._configure_custom_styles()

        # --- Toolbar (compact, top) ---
        toolbar = ttk.Frame(root, padding=6)
        toolbar.grid(row=0, column=0, sticky="ew")
        root.columnconfigure(0, weight=1)

        # compact toolbar: only global actions (file)
        open_btn = ttk.Button(toolbar, text=self.texts['open_file'], command=self.open_file)
        open_btn.grid(row=0, column=0, padx=(0,6))
        # 设置按钮字体
        open_btn.configure(style="Custom.TButton")

        # --- Main split: left 20% info/controls, right 80% plotting ---
        main_frame = ttk.Frame(root, padding=(6,6))
        main_frame.grid(row=2, column=0, sticky="nsew")
        root.rowconfigure(2, weight=1)
        main_frame.columnconfigure(0, weight=1)   # left panel (approx 20%)
        main_frame.columnconfigure(1, weight=4)   # right panel (approx 80%)
        main_frame.rowconfigure(0, weight=1)

        # Left panel: information & controls (stacked sections)
        left_panel = ttk.Frame(main_frame, padding=(6,6), relief="flat")
        left_panel.grid(row=0, column=0, sticky="nswe", padx=(0,6), pady=(0,0))
        left_panel.columnconfigure(0, weight=1)
        left_panel.rowconfigure(4, weight=1)  # Make the last row expandable

        # -- File information --
        file_frame = ttk.LabelFrame(left_panel, text=self.texts['file_info'], padding=(6,6))
        file_frame.grid(row=0, column=0, sticky="ew", pady=(0,8))
        file_frame.columnconfigure(0, weight=1)
        self.file_label = ttk.Label(file_frame, text=self.texts['no_file'], anchor="w")
        self.file_label.grid(row=0, column=0, sticky="w")
        # Add tooltip for full path
        self._create_tooltip(self.file_label, self.texts['no_file'])
        self.total_label = ttk.Label(file_frame, text=f"{self.texts['total_points']}: 0", anchor="w")
        self.total_label.grid(row=1, column=0, sticky="w", pady=(4,0))

        # -- Coordinates selection --
        coord_frame = ttk.LabelFrame(left_panel, text=self.texts['coord_selection'], padding=(6,6))
        coord_frame.grid(row=1, column=0, sticky="ew", pady=(0,8))
        coord_frame.columnconfigure(1, weight=1)
        ttk.Label(coord_frame, text="X:").grid(row=0, column=0, sticky="w", padx=(0,6))
        self.x_combo = ttk.Combobox(coord_frame, state="readonly", width=22)
        self.x_combo.grid(row=0, column=1, sticky="ew")
        ttk.Label(coord_frame, text="Y:").grid(row=1, column=0, sticky="w", padx=(0,6), pady=(6,0))
        self.y_combo = ttk.Combobox(coord_frame, state="readonly", width=22)
        self.y_combo.grid(row=1, column=1, sticky="ew", pady=(6,0))

        # -- Data filtering --
        filt_frame = ttk.LabelFrame(left_panel, text=self.texts['data_filter'], padding=(6,6))
        filt_frame.grid(row=2, column=0, sticky="ew")
        filt_frame.columnconfigure(1, weight=1)

        ttk.Label(filt_frame, text=f"{self.texts['filter_col']}:").grid(row=0, column=0, sticky="w")
        self.filter_col_cb = ttk.Combobox(filt_frame, state="readonly", values=[], width=20)
        self.filter_col_cb.grid(row=0, column=1, sticky="ew", padx=(6,0))

        ttk.Label(filt_frame, text=f"{self.texts['filter_mean']}:").grid(row=1, column=0, sticky="w", pady=(6,0))
        self.filter_mean_var = tk.StringVar(value="")
        self.filter_mean_entry = ttk.Entry(filt_frame, textvariable=self.filter_mean_var, width=10)
        self.filter_mean_entry.grid(row=1, column=1, sticky="w", padx=(6,0), pady=(6,0))

        # 容差
        ttk.Label(filt_frame, text=f"{self.texts['tolerance']}:").grid(row=2, column=0, sticky="w", pady=(6,0))
        self.filter_tol_var = tk.StringVar(value="0.2")
        self.filter_tol_entry = ttk.Entry(filt_frame, textvariable=self.filter_tol_var, width=8)
        self.filter_tol_entry.grid(row=2, column=1, sticky="w", padx=(6,0), pady=(6,0))
        
        # 最小连续行数 (换到下一行)
        ttk.Label(filt_frame, text=f"{self.texts['min_length']}:").grid(row=3, column=0, sticky="w", pady=(6,0))
        self.filter_minlen_var = tk.StringVar(value="10")
        self.filter_minlen_entry = ttk.Entry(filt_frame, textvariable=self.filter_minlen_var, width=8)
        self.filter_minlen_entry.grid(row=3, column=1, sticky="w", padx=(6,0), pady=(6,0))

        # detect button (integrated into filtering panel)
        self.detect_btn_left = ttk.Button(filt_frame, text=self.texts['filter_btn'], command=self.run_detect, style="Custom.TButton")
        self.detect_btn_left.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8,6))

        # detected segments list (tree)
        seg_cols = ("val", "std", "start", "end", "len")
        self.seg_tree = ttk.Treeview(filt_frame, columns=seg_cols, show="headings", height=8, style="Custom.Treeview")
        for c in seg_cols:
            # 平均值列左对齐，其他列右对齐
            anchor = "w" if c == "val" else "e"
            # enable header-click sorting by passing the column name to the sort handler
            self.seg_tree.heading(c, text=c, command=lambda _col=c: self._seg_tree_sort(_col), anchor=anchor)
            self.seg_tree.column(c, width=60, anchor=anchor)
        self.seg_tree.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=(6,6))
        filt_frame.rowconfigure(5, weight=1)
        # double-click on a row will set start/end entries
        self.seg_tree.bind("<Double-1>", self._on_seg_double_click)
        # single click (with optional Shift) for replace/overlay behavior
        self.seg_tree.bind("<ButtonRelease-1>", self._on_seg_click)

        # drawing range control
        draw_range_frame = ttk.LabelFrame(left_panel, text=self.texts['plot_range'], padding=(6,6))
        draw_range_frame.grid(row=3, column=0, sticky="ew", pady=(8,0))
        draw_range_frame.columnconfigure(1, weight=1)
        
        ttk.Label(draw_range_frame, text=f"{self.texts['start_row']}:").grid(row=0, column=0, sticky="w")
        self.start_var = tk.StringVar(value="1")
        self.start_entry = ttk.Entry(draw_range_frame, textvariable=self.start_var, width=8)
        self.start_entry.grid(row=0, column=1, sticky="w", padx=(6,0))
        
        ttk.Label(draw_range_frame, text=f"{self.texts['end_row']}:").grid(row=0, column=2, sticky="w", padx=(20,0))
        self.end_var = tk.StringVar(value="")
        self.end_entry = ttk.Entry(draw_range_frame, textvariable=self.end_var, width=8)
        self.end_entry.grid(row=0, column=3, sticky="w", padx=(6,0))

        # plot type radio buttons placed at bottom
        plot_type_frame = ttk.Frame(left_panel)
        plot_type_frame.grid(row=4, column=0, sticky="sew", pady=(6,0))
        ttk.Label(plot_type_frame, text=f"{self.texts['plot_type']}:").grid(row=0, column=0, sticky="w")
        self.plot_type_var = tk.StringVar(value="both")
        ttk.Radiobutton(plot_type_frame, text=self.texts['line_plot'], variable=self.plot_type_var, value="line", command=self._on_user_change).grid(row=0, column=1, sticky="w", padx=(6,0))
        ttk.Radiobutton(plot_type_frame, text=self.texts['scatter_plot'], variable=self.plot_type_var, value="scatter", command=self._on_user_change).grid(row=0, column=2, sticky="w", padx=(6,0))
        ttk.Radiobutton(plot_type_frame, text=self.texts['both_plot'], variable=self.plot_type_var, value="both", command=self._on_user_change).grid(row=0, column=3, sticky="w", padx=(6,0))

        # Right panel: plotting area
        right_panel = ttk.Frame(main_frame)
        right_panel.grid(row=0, column=1, sticky="nsew")
        right_panel.columnconfigure(0, weight=1)
        right_panel.rowconfigure(0, weight=1)

        # Use figure DPI tuned to system DPI and place canvas in right panel
        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=self.dpi)
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_panel)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        # status bar at bottom of main window
        status_frame = ttk.Frame(root)
        status_frame.grid(row=3, column=0, sticky="ew", padx=0, pady=(4,0))
        status_frame.columnconfigure(0, weight=1)
        status_frame.columnconfigure(1, weight=1)  # 版权信息也占据一定宽度
        
        self.status = ttk.Label(status_frame, text=self.texts['status_ready'], anchor="w", relief="sunken")
        self.status.grid(row=0, column=0, sticky="ew")
        
        # 版权信息 - 使用Text组件以便复制
        self.copyright_text = tk.Text(status_frame, height=1, relief="sunken", bd=1, 
                                     font=self.ui_font, wrap="none", state="normal")
        self.copyright_text.insert("1.0", self.texts['copyright'])
        self.copyright_text.config(state="disabled")  # 只读模式
        self.copyright_text.grid(row=0, column=1, sticky="ew", padx=(10,0))
        try:
            root.rowconfigure(3, weight=0)
        except Exception:
            pass

        # bindings for quick expert workflow (wire up comboboxes and entries)
        self.x_combo.bind("<<ComboboxSelected>>", lambda e: self._on_user_change())
        self.y_combo.bind("<<ComboboxSelected>>", lambda e: self._on_user_change())
        self.start_entry.bind("<Return>", lambda e: self._on_user_change())
        self.end_entry.bind("<Return>", lambda e: self._on_user_change())
        self.start_entry.bind("<FocusOut>", lambda e: self._on_user_change())
        self.end_entry.bind("<FocusOut>", lambda e: self._on_user_change())
        
        # bind mouse events for zoom functionality
        self.canvas.mpl_connect('button_press_event', self._on_mouse_press)
        self.canvas.mpl_connect('motion_notify_event', self._on_mouse_drag)
        self.canvas.mpl_connect('button_release_event', self._on_mouse_release)

    def _create_tooltip(self, widget, text):
        """Create a tooltip for a widget."""
        def on_enter(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            label = tk.Label(tooltip, text=text, background="lightyellow", 
                           relief="solid", borderwidth=1, font=("Arial", 9))
            label.pack()
            widget.tooltip = tooltip
        
        def on_leave(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                del widget.tooltip
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def _configure_custom_styles(self):
        """Configure custom styles for UI components."""
        style = ttk.Style()
        
        # 配置按钮样式
        style.configure("Custom.TButton", font=self.ui_font)
        
        # 配置标签样式
        style.configure("Custom.TLabel", font=self.ui_font)
        
        # 配置下拉框样式
        style.configure("Custom.TCombobox", font=self.ui_font)
        
        # 配置输入框样式
        style.configure("Custom.TEntry", font=self.ui_font)
        
        # 配置单选按钮样式
        style.configure("Custom.TRadiobutton", font=self.ui_font)
        
        # 配置树形视图样式
        treeview_font = ("Microsoft YaHei", int(self.ui_font_size * 0.9))
        style.configure("Custom.Treeview", font=treeview_font, rowheight=24)
        style.configure("Custom.Treeview.Heading", font=treeview_font)
        
        # 配置LabelFrame标题字体
        label_frame_font = ("Microsoft YaHei", self.ui_font_size, "bold")
        style.configure("TLabelframe.Label", font=label_frame_font)
        
        # 配置LabelFrame内容字体
        label_frame_content_font = ("Microsoft YaHei", int(self.ui_font_size * 0.9))
        style.configure("TLabelframe", font=label_frame_content_font)
        
        # 配置Combobox下拉列表字体
        style.configure("TCombobox", font=self.ui_font)
        style.configure("TCombobox.Listbox", font=self.ui_font)
        
        # 配置Entry输入框字体
        style.configure("TEntry", font=self.ui_font)
        
        # 配置所有基础组件的字体
        style.configure("TLabel", font=self.ui_font)
        style.configure("TButton", font=self.ui_font)
        style.configure("TRadiobutton", font=self.ui_font)

    def _show_progress_dialog(self, title):
        """Show a progress dialog."""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("400x120")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (dialog.winfo_screenheight() // 2) - (120 // 2)
        dialog.geometry(f"400x120+{x}+{y}")
        
        # Progress frame
        frame = ttk.Frame(dialog, padding=20)
        frame.pack(fill="both", expand=True)
        
        # Progress label
        progress_label = ttk.Label(frame, text=self.texts['progress_processing'], font=("Arial", 10))
        progress_label.pack(pady=(0, 10))
        
        # Progress bar
        progress_bar = ttk.Progressbar(frame, mode='determinate', length=350)
        progress_bar.pack(pady=(0, 10))
        progress_bar['value'] = 0
        
        # Store references
        dialog.progress_label = progress_label
        dialog.progress_bar = progress_bar
        
        return dialog
    
    def _update_progress(self, dialog, value, text):
        """Update progress dialog."""
        if dialog and dialog.winfo_exists():
            dialog.progress_bar['value'] = value
            dialog.progress_label.config(text=text)
            dialog.update_idletasks()
    
    def _close_progress_dialog(self, dialog):
        """Close progress dialog."""
        if dialog and dialog.winfo_exists():
            dialog.grab_release()
            dialog.destroy()

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("DAT files","*.dat"),("All files","*.*")])
        if not path:
            return
        self.filepath = path
        
        # Show progress dialog
        progress_dialog = self._show_progress_dialog(self.texts['progress_loading'])
        
        try:
            # Update progress
            self._update_progress(progress_dialog, 20, "正在读取文件头部...")
            header_lines, data_start_line = self._read_header(path)
            
            self._update_progress(progress_dialog, 40, "正在解析时间信息...")
            self._parse_fileopentime(header_lines)
            
            self._update_progress(progress_dialog, 60, "正在读取数据...")
            # read data starting at data_start_line (0-based index), header is at that line
            self.df = pd.read_csv(path, skiprows=data_start_line, header=0, engine='python')
            
            self._update_progress(progress_dialog, 80, "正在处理列名...")
            # strip column names
            self.df.columns = [c.strip() for c in self.df.columns]
            # handle duplicate or empty column names
            cols = []
            seen = {}
            for i,c in enumerate(self.df.columns):
                name = c if c != "" else f"Unnamed_{i}"
                if name in seen:
                    seen[name] += 1
                    name = f"{name}_{seen[name]}"
                else:
                    seen[name] = 0
                cols.append(name)
            self.df.columns = cols

            self._update_progress(progress_dialog, 90, "正在初始化界面...")
            self.x_combo['values'] = list(self.df.columns)
            self.y_combo['values'] = list(self.df.columns)
            # populate filter column combobox as well
            try:
                self.filter_col_cb['values'] = list(self.df.columns)
                # choose a sensible default: first numeric-like column if available
                default_filter = None
                for c in self.df.columns:
                    ser = pd.to_numeric(self.df[c], errors='coerce')
                    if ser.dropna().size > 0:
                        default_filter = c
                        break
                if default_filter is None:
                    default_filter = self.df.columns[0]
                    self.filter_col_cb.set(default_filter)
                # update file info labels
                try:
                    # Display only filename for long paths
                    filename = os.path.basename(self.filepath)
                    if len(self.filepath) > 50:  # If path is too long, show only filename
                        display_text = f"...{os.path.sep}{filename}"
                    else:
                        display_text = self.filepath
                    self.file_label.config(text=display_text)
                    # Update tooltip with full path
                    self._create_tooltip(self.file_label, self.filepath)
                    self.total_label.config(text=f"{self.texts['total_points']}: {len(self.df)}")
                except Exception:
                    pass
            except Exception:
                # ignore if filter combobox isn't available for some reason
                pass
            # defaults
            if "Time Stamp (sec)" in self.df.columns:
                self.x_combo.set("Time Stamp (sec)")
            else:
                self.x_combo.set(self.df.columns[0])
            if "Moment (emu)" in self.df.columns:
                self.y_combo.set("Moment (emu)")
            else:
                self.y_combo.set(self.df.columns[1] if len(self.df.columns)>1 else self.df.columns[0])

            # set default end to total rows
            self.start_var.set("1")
            self.end_var.set(str(len(self.df)))

            self._update_progress(progress_dialog, 95, "正在绘制初始图形...")
            self.status.config(text=f"{self.texts['status_file_loaded']}: {path}，行数: {len(self.df)}")

            # auto draw initial plot if possible
            try:
                self.draw_plot()
            except Exception:
                pass
            
            # Close progress dialog
            self._close_progress_dialog(progress_dialog)
            self.status.config(text=f"{self.texts['status_file_loaded']}: {os.path.basename(path)}，行数: {len(self.df)}")
            
        except Exception as e:
            self._close_progress_dialog(progress_dialog)
            messagebox.showerror("错误", f"打开文件失败: {e}")
            self.status.config(text=self.texts['error_file_format'])

    def _read_header(self, path):
        header_lines = []
        data_start = None
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for idx, line in enumerate(f):
                stripped = line.strip()
                header_lines.append(line.rstrip("\n"))
                if stripped == "[Data]":
                    # data header is next line (idx+1). We'll tell caller to skip rows up to idx+1
                    data_start = idx+1
                    break
        if data_start is None:
            raise ValueError("未找到 [Data] 段")
        return header_lines, data_start

    def _parse_fileopentime(self, header_lines):
        self.fileopentime_ts = None
        self.fileopentime_dt = None
        for ln in header_lines:
            if ln.startswith("FILEOPENTIME"):
                parts = ln.split(",", 3)
                # examples: FILEOPENTIME,3862854806.58759,05/27/2022,11:13 pm
                if len(parts) >= 2:
                    try:
                        self.fileopentime_ts = float(parts[1])
                    except:
                        self.fileopentime_ts = None
                if len(parts) >= 4:
                    date_str = parts[2].strip()
                    time_str = parts[3].strip()
                    # try parse like "05/27/2022" + "11:13 pm"
                    try:
                        self.fileopentime_dt = datetime.strptime(date_str + " " + time_str, "%m/%d/%Y %I:%M %p")
                    except Exception:
                        # try other common formats
                        try:
                            self.fileopentime_dt = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M:%S")
                        except:
                            self.fileopentime_dt = None
                break

    def _get_range_indices(self):
        # return (start_idx, end_idx) as python slice indices ([start_idx:end_idx])
        if self.df is None:
            return 0, 0
        n = len(self.df)
        try:
            s = int(self.start_var.get())
        except Exception:
            s = 1
        try:
            e = int(self.end_var.get())
        except Exception:
            e = n
        # clamp and convert 1-based inclusive to 0-based slice
        if s < 1:
            s = 1
        if e < 1:
            e = n
        if s > n:
            s = n
        if e > n:
            e = n
        if s > e:
            s, e = e, s
        start_idx = s - 1
        end_idx = e  # slice end is exclusive, but e is inclusive 1-based -> use e
        return start_idx, end_idx

    def _prepare_xy(self, xcol, ycol):
        if self.df is None:
            raise RuntimeError("未加载数据")
        # apply row range selection
        start_idx, end_idx = self._get_range_indices()
        df = self.df.iloc[start_idx:end_idx].copy()

        # if Time Stamp conversion requested and column is Time Stamp (sec)
        if self.convert_time_var.get():
            for col in (xcol, ycol):
                if col == "Time Stamp (sec)":
                    if self.fileopentime_ts is not None and self.fileopentime_dt is not None:
                        base_ts = self.fileopentime_ts
                        base_dt = self.fileopentime_dt
                        # compute dt series
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                        df[col] = df[col].apply(lambda v: (base_dt + timedelta(seconds=(v - base_ts))) if pd.notna(v) else pd.NaT)
                    else:
                        # fallback: try interpret as unix epoch seconds if values large (~1e9)
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                        sample = df[col].dropna()
                        if not sample.empty and sample.median() > 1e9:
                            df[col] = pd.to_datetime(df[col], unit='s', errors='coerce')
                        else:
                            # leave as numeric (seconds) if cannot convert
                            pass

        # convert non-datetime to numeric
        x_is_dt = pd.api.types.is_datetime64_any_dtype(df[xcol])
        y_is_dt = pd.api.types.is_datetime64_any_dtype(df[ycol])

        if not x_is_dt:
            df[xcol] = pd.to_numeric(df[xcol], errors='coerce')
        if not y_is_dt:
            df[ycol] = pd.to_numeric(df[ycol], errors='coerce')

        # drop rows with NaN in X or Y
        df_clean = df.dropna(subset=[xcol, ycol])
        dropped = len(df) - len(df_clean)
        return df_clean, dropped

    def draw_plot(self):
        if self.df is None:
            messagebox.showwarning("未加载数据", "请先打开 .dat 文件")
            return
        xcol = self.x_combo.get()
        ycol = self.y_combo.get()
        if not xcol or not ycol:
            messagebox.showwarning("选择列", "请从下拉框中选择 X 和 Y 列")
            return
        try:
            df, dropped = self._prepare_xy(xcol, ycol)
        except Exception as e:
            messagebox.showerror("错误", f"准备数据失败: {e}")
            return
        self.ax.clear()
        plot_t = self.plot_type_var.get()
        x = df[xcol]
        y = df[ycol]
        # plotting
        if plot_t in ("line","both"):
            self.ax.plot(x, y, label="line", lw=1)
        if plot_t in ("scatter","both"):
            self.ax.scatter(x, y, s=8, label="points")
        self.ax.set_xlabel(xcol)
        self.ax.set_ylabel(ycol)
        title = f"{ycol} vs {xcol}"
        if self.filepath:
            title = f"{title} — {os.path.basename(self.filepath)}"
        self.ax.set_title(title)
        self.ax.grid(True)
        if plot_t in ("both",):
            self.ax.legend()

        # format time axis if x is datetime
        if pd.api.types.is_datetime64_any_dtype(x):
            self.fig.autofmt_xdate()
        
        # Save initial zoom state when drawing new plot
        self._save_zoom_state()
        
        self.canvas.draw()
        start_idx, end_idx = self._get_range_indices()
        self.status.config(text=f"{self.texts['status_plot_drawn']}，行范围: {start_idx+1}-{end_idx}，点数: {len(df)}，剔除 {dropped} 行无效数据")


    def run_detect(self):
        """Run detection using the left-panel filter controls and populate seg_tree."""
        # clear previous
        try:
            for it in self.seg_tree.get_children():
                self.seg_tree.delete(it)
        except Exception:
            pass

        if self.df is None:
            messagebox.showwarning("未加载数据", "请先打开 .dat 文件")
            return

        col = self.filter_col_cb.get()
        if not col:
            messagebox.showwarning("请选择列", "请在筛选列中选择一列")
            return

        # parse tolerance and min length
        try:
            tol = float(self.filter_tol_var.get())
        except Exception:
            messagebox.showerror("容差错误", "容差必须为数字")
            return
        try:
            minlen = int(self.filter_minlen_var.get())
            if minlen < 1:
                minlen = 1
        except Exception:
            minlen = 10

        # get array
        arr_series = pd.to_numeric(self.df[col], errors='coerce')
        arr = arr_series.to_numpy(dtype=float)

        # if user provided a specific filter mean, select values near that mean using tol
        mean_text = self.filter_mean_var.get().strip()
        if mean_text != "":
            try:
                target = float(mean_text)
                # boolean mask of rows satisfying |value - target| <= tol
                mask = np.isfinite(arr) & (np.abs(arr - target) <= tol)
                # find contiguous runs in mask
                idx = np.where(mask)[0]
                segs = []
                if idx.size > 0:
                    breaks = np.where(np.diff(idx) != 1)[0]
                    if breaks.size == 0:
                        runs = [(idx[0], idx[-1])]
                    else:
                        runs = []
                        start = idx[0]
                        for b in breaks:
                            end = idx[b]
                            runs.append((start, end))
                            start = idx[b+1]
                        runs.append((start, idx[-1]))
                    for s, e in runs:
                        length = e - s + 1
                        if length >= minlen:
                            seg_arr = arr[s:e+1]
                            segs.append({'val': float(np.nanmean(seg_arr)), 'start': int(s+1), 'end': int(e+1), 'len': int(length), 'mean': float(np.nanmean(seg_arr)), 'std': float(np.nanstd(seg_arr))})
            except Exception:
                segs = []
        else:
            # use existing find_candidates implementation (which expects tol as absolute or relative via rel flag)
            segs = self.find_candidates(arr, tol, rel=False, min_length=minlen)
        if not segs:
            messagebox.showinfo("无结果", "未找到满足条件的连续段，请调大容差或减小最短长度。")
            self.status.config(text=f"{self.texts['status_plot_drawn']}: {self.texts['error_no_data']}")
            return

        # populate tree
        for i, s in enumerate(segs):
            # tree columns: val, std, start, end, len
            # 平均值最多显示5位字符，标准差最多显示5位字符
            val_str = f"{s['val']:.4g}"[:5] if len(f"{s['val']:.4g}") > 5 else f"{s['val']:.4g}"
            std_str = f"{s['std']:.4g}"[:5] if len(f"{s['std']:.4g}") > 5 else f"{s['std']:.4g}"
            self.seg_tree.insert('', 'end', iid=str(i), values=(val_str, std_str, s['start'], s['end'], s['len']))
        self.status.config(text=f"{self.texts['status_plot_drawn']}: 发现 {len(segs)} 段")

    def _on_seg_double_click(self, event):
        """Handle double-click on seg_tree: set start/end entries to the clicked row's values and redraw."""
        try:
            sel = self.seg_tree.selection()
            if not sel:
                return
            iid = sel[0]
            vals = self.seg_tree.item(iid, 'values')
            # values layout: val, std, start, end, len
            start = vals[2]
            end = vals[3]
            self.start_var.set(str(start))
            self.end_var.set(str(end))
            # trigger redraw
            try:
                self.draw_plot()
            except Exception:
                pass
        except Exception:
            pass

    def _get_xy_for_segment(self, start_row, end_row):
        """Return x,y arrays for a segment given 1-based start_row and end_row (inclusive)."""
        if self.df is None:
            return None, None
        # convert to 0-based indices
        s = max(0, int(start_row) - 1)
        e = max(0, int(end_row) - 1)
        # clamp
        n = len(self.df)
        s = min(max(0, s), n-1)
        e = min(max(0, e), n-1)
        if s > e:
            s, e = e, s
        xcol = self.x_combo.get()
        ycol = self.y_combo.get()
        if not xcol or not ycol:
            return None, None
        sub = self.df.iloc[s:e+1].copy()
        # apply time conversion if set
        if self.convert_time_var.get():
            if xcol == "Time Stamp (sec)":
                try:
                    base_ts = self.fileopentime_ts
                    base_dt = self.fileopentime_dt
                    if base_ts is not None and base_dt is not None:
                        sub[xcol] = pd.to_numeric(sub[xcol], errors='coerce')
                        sub[xcol] = sub[xcol].apply(lambda v: (base_dt + timedelta(seconds=(v - base_ts))) if pd.notna(v) else pd.NaT)
                except Exception:
                    pass
        # coerce to numeric if possible
        try:
            if not pd.api.types.is_datetime64_any_dtype(sub[xcol]):
                sub[xcol] = pd.to_numeric(sub[xcol], errors='coerce')
        except Exception:
            pass
        try:
            if not pd.api.types.is_datetime64_any_dtype(sub[ycol]):
                sub[ycol] = pd.to_numeric(sub[ycol], errors='coerce')
        except Exception:
            pass
        sub = sub.dropna(subset=[xcol, ycol])
        return sub[xcol].to_numpy(), sub[ycol].to_numpy()

    def _clear_overlays(self):
        """Remove overlay artists from the axes and clear state."""
        try:
            for iid, artists in list(self._overlay_artists.items()):
                for a in artists:
                    try:
                        a.remove()
                    except Exception:
                        pass
                # remove tag if any
                try:
                    self.seg_tree.tag_remove('overlayed', iid)
                except Exception:
                    pass
            self._overlay_artists.clear()
            self.canvas.draw()
        except Exception:
            pass

    def _plot_segment(self, iid, overlay=False):
        """Plot a segment identified by tree iid. overlay=False replaces main plot, True overlays."""
        try:
            vals = self.seg_tree.item(iid, 'values')
            start = int(vals[2])
            end = int(vals[3])
        except Exception:
            return
        x, y = self._get_xy_for_segment(start, end)
        if x is None or y is None:
            return
        plot_t = self.plot_type_var.get() if hasattr(self, 'plot_type_var') else 'both'
        artists = []
        if not overlay:
            # clear overlays and main axes
            self._clear_overlays()
            try:
                self.ax.clear()
            except Exception:
                pass
        # draw according to plot type
        if plot_t in ('line', 'both'):
            try:
                ln, = self.ax.plot(x, y, label=f"seg_{iid}")
                artists.append(ln)
            except Exception:
                pass
        if plot_t in ('scatter', 'both'):
            try:
                sc = self.ax.scatter(x, y, s=10)
                artists.append(sc)
            except Exception:
                pass
        # store overlay artists if overlay True
        if overlay:
            self._overlay_artists[iid] = artists
            try:
                self.seg_tree.tag_configure('overlayed', background='#fff2cc')
                self.seg_tree.item(iid, tags=('overlayed',))
            except Exception:
                pass
        else:
            # replace: mark this as active (clear overlay tags)
            try:
                for it in self.seg_tree.get_children(''):
                    self.seg_tree.item(it, tags=())
            except Exception:
                pass
        try:
            self.ax.relim()
            self.ax.autoscale_view()
            self.canvas.draw()
        except Exception:
            try:
                self.canvas.draw()
            except Exception:
                pass

    def _on_seg_click(self, event):
        """Handle single click on seg_tree rows; overlay if Shift held, else replace."""
        # determine item under pointer
        try:
            iid = self.seg_tree.identify_row(event.y)
            if not iid:
                return
            # detect shift: prefer event.state but fallback to key tracking
            shift = False
            try:
                shift = bool(event.state & 0x0001)
            except Exception:
                # fallback: use tkinter key state (not implemented here)
                shift = False
            if shift:
                # overlay toggle
                if iid in self._overlay_artists:
                    # remove overlay
                    for a in self._overlay_artists.get(iid, []):
                        try:
                            a.remove()
                        except Exception:
                            pass
                    try:
                        self.seg_tree.item(iid, tags=())
                    except Exception:
                        pass
                    try:
                        del self._overlay_artists[iid]
                    except Exception:
                        pass
                    try:
                        self.canvas.draw()
                    except Exception:
                        pass
                else:
                    # add overlay
                    if len(self._overlay_artists) >= self._max_overlays:
                        messagebox.showinfo('提示', f'最多允许 {self._max_overlays} 个叠加段')
                        return
                    self._plot_segment(iid, overlay=True)
            else:
                # replace mode
                self._plot_segment(iid, overlay=False)
        except Exception:
            pass

    def _seg_tree_sort(self, col):
        """Sort the seg_tree by column `col` (one of the seg_cols names)."""
        try:
            # get all items
            items = [(self.seg_tree.set(k, col), k) for k in self.seg_tree.get_children('')]
            # try numeric sort
            def _num(x):
                try:
                    return float(x)
                except Exception:
                    return x
            items.sort(key=lambda t: _num(t[0]))
            # reorder
            for index, (_, k) in enumerate(items):
                self.seg_tree.move(k, '', index)
        except Exception:
            pass

    def _on_user_change(self):
        # try to redraw automatically; ignore errors silently
        if self.df is None:
            return
        try:
            self.draw_plot()
        except Exception:
            pass

    def _on_mouse_press(self, event):
        """Handle mouse press events for zoom functionality."""
        if event.inaxes != self.ax:
            return
        
        if event.button == 1:  # Left click - start selection
            self._is_selecting = True
            self._select_start = (event.xdata, event.ydata)
            self._select_end = None
            # Clear any existing selection rectangle
            if self._selection_rect:
                try:
                    self._selection_rect.remove()
                except:
                    pass
                self._selection_rect = None
        elif event.button == 3:  # Right click - zoom back
            self._zoom_back()
    
    def _on_mouse_drag(self, event):
        """Handle mouse drag events for selection rectangle."""
        if not self._is_selecting or event.inaxes != self.ax:
            return
        
        if event.xdata is None or event.ydata is None:
            return
        
        self._select_end = (event.xdata, event.ydata)
        
        # Update selection rectangle
        if self._select_start and self._select_end:
            # Clear previous rectangle
            if self._selection_rect:
                try:
                    self._selection_rect.remove()
                except:
                    pass
            
            # Create new rectangle
            x1, y1 = self._select_start
            x2, y2 = self._select_end
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            x = min(x1, x2)
            y = min(y1, y2)
            
            self._selection_rect = self.ax.add_patch(
                plt.Rectangle((x, y), width, height, 
                            fill=False, edgecolor='blue', alpha=0.5, linewidth=2)
            )
            self.canvas.draw_idle()
    
    def _on_mouse_release(self, event):
        """Handle mouse release events for zoom functionality."""
        if not self._is_selecting or event.inaxes != self.ax:
            self._is_selecting = False
            return
        
        if event.button == 1:  # Left click release
            if self._select_start and self._select_end:
                # Apply zoom to selected area
                self._apply_zoom_selection()
            
            # Clean up selection
            self._is_selecting = False
            self._select_start = None
            self._select_end = None
            if self._selection_rect:
                try:
                    self._selection_rect.remove()
                except:
                    pass
                self._selection_rect = None
                self.canvas.draw_idle()

    def _apply_zoom_selection(self):
        """Apply zoom to the selected area."""
        if not self._select_start or not self._select_end:
            return
        
        # Save current view state before zooming
        self._save_zoom_state()
        
        # Get selection bounds
        x1, y1 = self._select_start
        x2, y2 = self._select_end
        
        # Ensure proper ordering
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        
        # Add small margin to prevent edge clipping
        x_range = x_max - x_min
        y_range = y_max - y_min
        margin_x = x_range * 0.05 if x_range > 0 else 1
        margin_y = y_range * 0.05 if y_range > 0 else 1
        
        x_min -= margin_x
        x_max += margin_x
        y_min -= margin_y
        y_max += margin_y
        
        # Apply zoom
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
        self.canvas.draw()
        
        # Update status
        self.status.config(text=f"{self.texts['status_zoom_applied']}: X[{x_min:.3g}, {x_max:.3g}], Y[{y_min:.3g}, {y_max:.3g}]")
    
    def _save_zoom_state(self):
        """Save current zoom state to history stack."""
        try:
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self._zoom_stack.append((xlim, ylim))
            
            # Limit stack size to prevent memory issues
            if len(self._zoom_stack) > 20:
                self._zoom_stack.pop(0)
        except Exception:
            pass
    
    def _zoom_back(self):
        """Zoom back to previous view state."""
        if not self._zoom_stack:
            self.status.config(text=self.texts['status_no_zoom_history'])
            return
        
        try:
            # Restore previous state
            xlim, ylim = self._zoom_stack.pop()
            self.ax.set_xlim(xlim)
            self.ax.set_ylim(ylim)
            self.canvas.draw()
            
            # Update status
            remaining = len(self._zoom_stack)
            self.status.config(text=f"已回退到上一级视图 (剩余历史: {remaining})")
        except Exception:
            self.status.config(text="回退失败")
    

    # --- New: detect dialog & logic (no external coding required by user) ---
    def open_detect_dialog(self):
        if self.df is None:
            messagebox.showwarning("未加载数据", "请先打开 .dat 文件")
            return

        dlg = tk.Toplevel(self.root)
        dlg.title("检测约为恒定值的连续段")
        dlg.geometry("760x480")
        frm = ttk.Frame(dlg, padding=8)
        frm.pack(fill="both", expand=True)

        # Controls row
        ctrl = ttk.Frame(frm)
        ctrl.pack(fill="x", pady=(0,6))

        ttk.Label(ctrl, text="约束列:").pack(side="left")
        col_cb = ttk.Combobox(ctrl, values=list(self.df.columns), state="readonly", width=30)
        col_cb.pack(side="left", padx=(4,8))
        col_cb.set(self.df.columns[0])

        ttk.Label(ctrl, text="容差:").pack(side="left")
        tol_var = tk.StringVar(value="0.001")
        tol_entry = ttk.Entry(ctrl, textvariable=tol_var, width=10)
        tol_entry.pack(side="left", padx=(4,4))

        mode_var = tk.StringVar(value="abs")
        mode_cb = ttk.Combobox(ctrl, values=["abs", "%"], state="readonly", width=6, textvariable=mode_var)
        mode_cb.pack(side="left", padx=(0,8))

        ttk.Label(ctrl, text="最短长度:").pack(side="left")
        minlen_var = tk.StringVar(value="5")
        minlen_entry = ttk.Entry(ctrl, textvariable=minlen_var, width=6)
        minlen_entry.pack(side="left", padx=(4,8))

        detect_btn = ttk.Button(ctrl, text="检测", width=10)
        detect_btn.pack(side="left")

        auto_btn = ttk.Button(ctrl, text="自动选择最长段", width=18)
        auto_btn.pack(side="left", padx=(6,0))

        # Results tree
        cols = ("val", "start", "end", "len", "mean", "std")
        tree = ttk.Treeview(frm, columns=cols, show="headings", selectmode="browse", height=18)
        for c in cols:
            # 平均值列左对齐，其他列右对齐
            anchor = "w" if c in ["val", "mean"] else "e"
            tree.heading(c, text=c, anchor=anchor)
            tree.column(c, width=100, anchor=anchor)
        tree.pack(fill="both", expand=True)

        # Buttons
        btnf = ttk.Frame(frm)
        btnf.pack(fill="x", pady=(6,0))
        preview_btn = ttk.Button(btnf, text="预览选中段")
        use_btn = ttk.Button(btnf, text="使用选中段（写入 Start/Finish）")
        close_btn = ttk.Button(btnf, text="关闭")
        preview_btn.pack(side="left", padx=6)
        use_btn.pack(side="left", padx=6)
        close_btn.pack(side="right", padx=6)

        # Internal state of detected segments
        detected_segments = []

        def find_candidates(arr, tol_abs, rel=False, min_length=5, merge_gap=0):
            # arr: 1D numpy array with possible nan
            # returns list of segments dicts: {'val':v,'start':s,'end':e,'len':L,'mean':m,'std':sd}
            n = arr.shape[0]
            mask_valid = np.isfinite(arr)
            if not mask_valid.any():
                return []
            a = arr.copy()
            # compute effective tol_abs when rel=True
            if rel:
                scale = np.nanmedian(np.abs(a[mask_valid]))
                tol = abs(tol_abs * (scale if scale != 0 else 1.0))
            else:
                tol = abs(tol_abs)
            if tol == 0:
                tol = 1e-12

            # bucket by rounding to tol
            buckets = np.full(n, np.nan)
            buckets[mask_valid] = np.round(a[mask_valid] / tol) * tol
            unique_buckets = np.unique(buckets[mask_valid])

            segs = []
            for v in unique_buckets:
                mask = mask_valid & (np.abs(a - v) <= tol)
                if not mask.any():
                    continue
                # find contiguous True runs
                idx = np.where(mask)[0]
                # find breaks
                breaks = np.where(np.diff(idx) != 1)[0]
                if breaks.size == 0:
                    runs = [(idx[0], idx[-1])]
                else:
                    runs = []
                    start = idx[0]
                    for b in breaks:
                        end = idx[b]
                        runs.append((start, end))
                        start = idx[b+1]
                    runs.append((start, idx[-1]))
                # optionally merge close runs (not used now)
                for s, e in runs:
                    length = e - s + 1
                    if length >= min_length:
                        seg_arr = a[s:e+1]
                        seg_mean = float(np.nanmean(seg_arr))
                        seg_std = float(np.nanstd(seg_arr))
                        segs.append({'val': float(v), 'start': int(s+1), 'end': int(e+1),
                                     'len': int(length), 'mean': seg_mean, 'std': seg_std})
            # sort by length desc
            segs.sort(key=lambda x: x['len'], reverse=True)
            return segs

        def run_detect():
            nonlocal detected_segments
            tree.delete(*tree.get_children())
            detected_segments = []
            col = col_cb.get()
            if col == "":
                messagebox.showwarning("请选择列", "请先选择约束列")
                return
            try:
                tol = float(tol_var.get())
            except Exception:
                messagebox.showerror("错误", "容差必须为数字")
                return
            rel = (mode_var.get() == "%")
            try:
                minlen = int(minlen_var.get())
                if minlen < 1:
                    minlen = 1
            except Exception:
                minlen = 5
            # prepare array (use full df)
            arr = pd.to_numeric(self.df[col], errors='coerce').to_numpy(dtype=float)
            segs = find_candidates(arr, tol, rel=rel, min_length=minlen)
            if not segs:
                messagebox.showinfo("无结果", "未找到满足条件的连续段，请调大容差或减小最短长度。")
                return
            detected_segments = segs
            # populate tree
            for i,s in enumerate(segs):
                # 统一格式化：平均值最多5位字符，标准差最多5位字符
                val_str = f"{s['val']:.4g}"[:5] if len(f"{s['val']:.4g}") > 5 else f"{s['val']:.4g}"
                mean_str = f"{s['mean']:.4g}"[:5] if len(f"{s['mean']:.4g}") > 5 else f"{s['mean']:.4g}"
                std_str = f"{s['std']:.4g}"[:5] if len(f"{s['std']:.4g}") > 5 else f"{s['std']:.4g}"
                tree.insert("", "end", iid=str(i), values=(val_str, s['start'], s['end'], s['len'],
                                                           mean_str, std_str))
            self.status.config(text=f"检测完成，发现 {len(segs)} 段（显示全部）")

        def preview_selected():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("未选择", "请在列表中选择一段")
                return
            idx = int(sel[0])
            seg = detected_segments[idx]
            # compute x values for this start/end using current X column conversion
            xcol = self.x_combo.get()
            if xcol == "":
                messagebox.showwarning("未选择 X 列", "请先在主界面选择 X 列以便预览")
                return
            s_row = seg['start'] - 1
            e_row = seg['end'] - 1
            try:
                x_start = self._convert_single_value_to_axis(xcol, self.df.iloc[s_row][xcol])
                x_end = self._convert_single_value_to_axis(xcol, self.df.iloc[e_row][xcol])
            except Exception as ex:
                messagebox.showerror("预览失败", f"无法读取 X 值: {ex}")
                return
            # clear previous preview
            if self._preview_patch is not None:
                try:
                    self._preview_patch.remove()
                except Exception:
                    pass
                self._preview_patch = None
            # draw patch
            try:
                xmin, xmax = (x_start, x_end) if x_start <= x_end else (x_end, x_start)
                self._preview_patch = self.ax.axvspan(xmin, xmax, color='yellow', alpha=0.25)
                self.canvas.draw()
            except Exception as ex:
                messagebox.showerror("预览失败", f"在图上高亮失败: {ex}")

        def use_selected():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("未选择", "请在列表中选择一段")
                return
            idx = int(sel[0])
            seg = detected_segments[idx]
            # write into Start/Finish (1-based) and redraw
            self.start_var.set(str(seg['start']))
            self.end_var.set(str(seg['end']))
            # remove preview patch after applying
            if self._preview_patch is not None:
                try:
                    self._preview_patch.remove()
                except Exception:
                    pass
                self._preview_patch = None
            self.draw_plot()
            dlg.destroy()

        def auto_select_longest():
            run_detect()
            if not detected_segments:
                return
            # first segment is longest due to sorting
            seg = detected_segments[0]
            self.start_var.set(str(seg['start']))
            self.end_var.set(str(seg['end']))
            # close dialog and redraw
            dlg.destroy()
            self.draw_plot()

        detect_btn.config(command=run_detect)
        preview_btn.config(command=preview_selected)
        use_btn.config(command=use_selected)
        auto_btn.config(command=auto_select_longest)
        close_btn.config(command=lambda: (self._clear_preview(), dlg.destroy()))

        # ensure preview cleared on close
        dlg.protocol("WM_DELETE_WINDOW", lambda: (self._clear_preview(), dlg.destroy()))

    def _convert_single_value_to_axis(self, col, raw):
        # ...existing GUI-dependent helper (kept as placeholder)...
        raise NotImplementedError
         

    def _clear_preview(self):
        # GUI preview clear placeholder
        return
         

    # --- New: compact settings dialog for expert mode ---
    def open_settings(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("设置")
        dlg.resizable(False, False)
        frm = ttk.Frame(dlg, padding=8)
        frm.grid(sticky="nsew")

        ttk.Label(frm, text="图形类型:").grid(row=0, column=0, sticky="e", padx=(0,6))
        plot_cb = ttk.Combobox(frm, state="readonly", values=["scatter","line","both"], textvariable=self.plot_type_var, width=12)
        plot_cb.grid(row=0, column=1, sticky="w")

        time_cb = ttk.Checkbutton(frm, text="将 Time Stamp (sec) 转为可读时间", variable=self.convert_time_var)
        time_cb.grid(row=1, column=0, columnspan=2, sticky="w", pady=(6,0))

        ttk.Label(frm, text="（FILEOPENTIME 会被用于基准映射）").grid(row=2, column=0, columnspan=2, sticky="w", pady=(4,6))

        btn_frame = ttk.Frame(frm)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=(6,0))
        ttk.Button(btn_frame, text="应用并关闭", command=lambda: (self._on_user_change(), dlg.destroy())).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="取消", command=dlg.destroy).pack(side="left", padx=4)

    def find_candidates(self, arr, tol, rel=False, min_length=3):
        """
        Detect contiguous segments in a 1D numeric numpy array `arr` where values
        are approximately constant within tolerance `tol`.

        Args:
            arr: 1D numpy array (may contain np.nan)
            tol: numeric tolerance. If rel is True, tol is relative fraction (e.g. 0.05)
            rel: whether tol is relative (fraction of median magnitude) or absolute
            min_length: minimum segment length (in rows) to return

        Returns:
            list of dicts: [{'val':..., 'start':1-based start, 'end':1-based end, 'len':..., 'mean':..., 'std':...}, ...]

        Notes:
            - contiguous means adjacent indices in the original array (NaN breaks segments)
            - start/end are 1-based inclusive as expected by tests
        """
        # normalize input
        if arr is None:
            return []
        a = np.asarray(arr, dtype=float)
        n = a.size
        if n == 0:
            return []

        # compute absolute tolerance
        finite = np.isfinite(a)
        if not np.any(finite):
            return []
        a_finite = a[finite]
        if rel:
            base = np.nanmedian(np.abs(a_finite))
            if base == 0 or not np.isfinite(base):
                base = np.nanmax(np.abs(a_finite))
            tol_abs = float(tol) * (base if base != 0 else 1.0)
        else:
            tol_abs = float(tol)

        # scan array to find contiguous runs of finite values and within-run value spread <= 2*tol_abs
        segments = []
        i = 0
        while i < n:
            if not finite[i]:
                i += 1
                continue
            # start a run at i
            j = i
            values = [a[i]]
            current_min = a[i]
            current_max = a[i]
            j += 1
            while j < n and finite[j]:
                v = a[j]
                new_min = min(current_min, v)
                new_max = max(current_max, v)
                # allow the run to include new value if total spread stays within allowed range
                if (new_max - new_min) <= (2 * tol_abs + 1e-12):
                    values.append(v)
                    current_min = new_min
                    current_max = new_max
                    j += 1
                else:
                    break
            run_len = len(values)
            if run_len >= min_length:
                mean = float(np.mean(values))
                std = float(np.std(values, ddof=0))
                # choose representative value as rounded mean where appropriate
                seg_val = float(np.round(mean, 6))
                segments.append({
                    'val': seg_val,
                    'start': i + 1,      # 1-based
                    'end': j,            # 1-based inclusive (j is next index, so j is end index)
                    'len': run_len,
                    'mean': mean,
                    'std': std
                })
            # move to next index after this run (advance by at least 1)
            i = j if j > i else i + 1

        # optionally sort segments by length desc, then by start asc
        segments.sort(key=lambda s: (-s['len'], s['start']))
        return segments

if __name__ == "__main__":
    # enable DPI awareness before creating the Tk root
    set_dpi_awareness()
    system_dpi = get_system_dpi()
    scaling = system_dpi / 96.0

    root = tk.Tk()
    # set Tcl/Tk scaling so built-in widgets/fonts scale on high-DPI
    try:
        root.tk.call('tk', 'scaling', scaling)
    except Exception:
        pass

    app = DatPlotterApp(root, dpi=system_dpi, scaling=scaling)
    root.mainloop()