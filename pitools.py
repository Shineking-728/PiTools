import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
import string
from datetime import datetime, timedelta
import re
import platform

class UtilityToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("多功能实用工具集")
        self.root.geometry("850x600")
        self.root.minsize(800, 550)

        # 设置中文字体支持
        self.style = ttk.Style()
        self.style.configure("TNotebook.Tab", font=("Microsoft YaHei", 10))
        self.style.configure("TButton", font=("Microsoft YaHei", 10))
        self.style.configure("TLabel", font=("Microsoft YaHei", 10))
        self.style.configure("TEntry", font=("Microsoft YaHei", 10))
        self.style.configure("TCheckbutton", font=("Microsoft YaHei", 10))
        self.style.configure("TRadiobutton", font=("Microsoft YaHei", 10))

        # 先创建状态栏，确保在其他方法调用前初始化
        self.status_bar = ttk.Label(root, text="就绪", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # 创建标签页容器
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 创建各个功能标签页
        self.create_text_tool_tab()
        self.create_calculator_tab()
        self.create_unit_converter_tab()
        self.create_password_generator_tab()
        self.create_datetime_tool_tab()
        self.create_text_analyzer_tab()

    # ------------------------------
    # 文本处理工具标签页
    # ------------------------------
    def create_text_tool_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="文本处理")

        # 左侧输入区域
        input_frame = ttk.LabelFrame(tab, text="输入文本")
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.text_input = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, width=40, height=20)
        self.text_input.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 中间按钮区域
        button_frame = ttk.Frame(tab)
        button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        ttk.Button(button_frame, text="转为大写", command=self.text_to_upper).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="转为小写", command=self.text_to_lower).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="首字母大写", command=self.text_to_title).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="反转文本", command=self.text_reverse).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="统计字数", command=self.count_words).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="清除空格", command=self.remove_spaces).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="复制结果", command=self.copy_result).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="清除", command=self.clear_text).pack(fill=tk.X, pady=2)

        # 右侧输出区域
        output_frame = ttk.LabelFrame(tab, text="处理结果")
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.text_output = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=40, height=20)
        self.text_output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # 文本处理功能实现（简单函数）
    def text_to_upper(self):
        text = self.text_input.get("1.0", tk.END).rstrip()
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, text.upper())
        self.status_bar.config(text="已完成：转为大写")

    def text_to_lower(self):
        text = self.text_input.get("1.0", tk.END).rstrip()
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, text.lower())
        self.status_bar.config(text="已完成：转为小写")

    def text_to_title(self):
        text = self.text_input.get("1.0", tk.END).rstrip()
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, text.title())
        self.status_bar.config(text="已完成：首字母大写")

    def text_reverse(self):
        text = self.text_input.get("1.0", tk.END).rstrip()
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, text[::-1])
        self.status_bar.config(text="已完成：反转文本")

    def count_words(self):
        text = self.text_input.get("1.0", tk.END).rstrip()
        char_count = len(text)
        word_count = len(text.split()) if text else 0
        line_count = text.count('\n') + 1 if text else 0
        result = f"字符数: {char_count}\n单词数: {word_count}\n行数: {line_count}"
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, result)
        self.status_bar.config(text="已完成：字数统计")

    def remove_spaces(self):
        text = self.text_input.get("1.0", tk.END).rstrip()
        cleaned = re.sub(r'\s+', ' ', text).strip()
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, cleaned)
        self.status_bar.config(text="已完成：清除多余空格")

    def copy_result(self):
        result = self.text_output.get("1.0", tk.END).rstrip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            messagebox.showinfo("提示", "已复制到剪贴板")
            self.status_bar.config(text="已复制结果到剪贴板")

    def clear_text(self):
        self.text_input.delete("1.0", tk.END)
        self.text_output.delete("1.0", tk.END)
        self.status_bar.config(text="已清除文本内容")

    # ------------------------------
    # 计算器标签页
    # ------------------------------
    def create_calculator_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="计算器")

        # 显示区域
        self.calc_expression = tk.StringVar()
        ttk.Label(tab, textvariable=self.calc_expression, font=("Microsoft YaHei", 16),
                  anchor=tk.E, background="#f0f0f0", padding=10).pack(fill=tk.X, padx=20, pady=10)

        # 按钮区域
        buttons_frame = ttk.Frame(tab)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 第一行
        ttk.Button(buttons_frame, text="C", command=self.clear_calculator).grid(row=0, column=0, padx=5, pady=5,
                                                                                sticky="nsew")
        ttk.Button(buttons_frame, text="←", command=self.backspace).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="%", command=lambda: self.add_to_expression("%")).grid(row=0, column=2, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="/", command=lambda: self.add_to_expression("/")).grid(row=0, column=3, padx=5,
                                                                                              pady=5, sticky="nsew")

        # 第二行
        ttk.Button(buttons_frame, text="7", command=lambda: self.add_to_expression("7")).grid(row=1, column=0, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="8", command=lambda: self.add_to_expression("8")).grid(row=1, column=1, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="9", command=lambda: self.add_to_expression("9")).grid(row=1, column=2, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="*", command=lambda: self.add_to_expression("*")).grid(row=1, column=3, padx=5,
                                                                                              pady=5, sticky="nsew")

        # 第三行
        ttk.Button(buttons_frame, text="4", command=lambda: self.add_to_expression("4")).grid(row=2, column=0, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="5", command=lambda: self.add_to_expression("5")).grid(row=2, column=1, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="6", command=lambda: self.add_to_expression("6")).grid(row=2, column=2, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="-", command=lambda: self.add_to_expression("-")).grid(row=2, column=3, padx=5,
                                                                                              pady=5, sticky="nsew")

        # 第四行
        ttk.Button(buttons_frame, text="1", command=lambda: self.add_to_expression("1")).grid(row=3, column=0, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="2", command=lambda: self.add_to_expression("2")).grid(row=3, column=1, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="3", command=lambda: self.add_to_expression("3")).grid(row=3, column=2, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="+", command=lambda: self.add_to_expression("+")).grid(row=3, column=3, padx=5,
                                                                                              pady=5, sticky="nsew")

        # 第五行
        ttk.Button(buttons_frame, text="±", command=self.toggle_sign).grid(row=4, column=0, padx=5, pady=5,
                                                                           sticky="nsew")
        ttk.Button(buttons_frame, text="0", command=lambda: self.add_to_expression("0")).grid(row=4, column=1, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text=".", command=lambda: self.add_to_expression(".")).grid(row=4, column=2, padx=5,
                                                                                              pady=5, sticky="nsew")
        ttk.Button(buttons_frame, text="=", command=self.calculate_result).grid(row=4, column=3, padx=5, pady=5,
                                                                                sticky="nsew")

        # 设置网格权重，使按钮可以扩展
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

    # 计算器功能实现（简单函数）
    def add_to_expression(self, value):
        current = self.calc_expression.get()
        self.calc_expression.set(current + str(value))
        self.status_bar.config(text=f"输入: {value}")

    def clear_calculator(self):
        self.calc_expression.set("")
        self.status_bar.config(text="计算器已清除")

    def backspace(self):
        current = self.calc_expression.get()
        self.calc_expression.set(current[:-1])
        self.status_bar.config(text="已删除最后一个字符")

    def toggle_sign(self):
        current = self.calc_expression.get()
        if current and current[0] == '-':
            self.calc_expression.set(current[1:])
        elif current:
            self.calc_expression.set('-' + current)
        self.status_bar.config(text="已切换正负号")

    def calculate_result(self):
        try:
            expression = self.calc_expression.get()
            # 替换百分号为百分比计算
            expression = expression.replace('%', '/100')
            result = eval(expression)
            # 处理浮点数显示
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.calc_expression.set(str(result))
            self.status_bar.config(text="计算完成")
        except Exception as e:
            self.calc_expression.set("错误")
            self.status_bar.config(text="计算错误")

    # ------------------------------
    # 单位转换工具标签页
    # ------------------------------
    def create_unit_converter_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="单位转换")

        # 创建转换类型选择
        conversion_frame = ttk.LabelFrame(tab, text="转换类型")
        conversion_frame.pack(fill=tk.X, padx=10, pady=5)

        self.conversion_type = tk.StringVar(value="长度")
        ttk.Radiobutton(conversion_frame, text="长度", variable=self.conversion_type, value="长度",
                        command=self.update_unit_options).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(conversion_frame, text="重量", variable=self.conversion_type, value="重量",
                        command=self.update_unit_options).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(conversion_frame, text="温度", variable=self.conversion_type, value="温度",
                        command=self.update_unit_options).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(conversion_frame, text="面积", variable=self.conversion_type, value="面积",
                        command=self.update_unit_options).pack(side=tk.LEFT, padx=10)

        # 创建转换输入区域
        input_frame = ttk.Frame(tab)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(input_frame, text="输入值:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.conversion_value = ttk.Entry(input_frame, width=20)
        self.conversion_value.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="从:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.from_unit = ttk.Combobox(input_frame, width=15)
        self.from_unit.grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(input_frame, text="转换", command=self.convert_units).grid(row=0, column=4, padx=10, pady=5)

        ttk.Label(input_frame, text="到:").grid(row=0, column=5, padx=5, pady=5, sticky=tk.W)
        self.to_unit = ttk.Combobox(input_frame, width=15)
        self.to_unit.grid(row=0, column=6, padx=5, pady=5)

        # 创建结果区域
        result_frame = ttk.LabelFrame(tab, text="转换结果")
        result_frame.pack(fill=tk.X, padx=10, pady=5)

        self.conversion_result = tk.StringVar()
        ttk.Label(result_frame, textvariable=self.conversion_result, font=("Microsoft YaHei", 12)).pack(padx=5, pady=5,
                                                                                                        anchor=tk.W)

        # 初始化单位选项
        self.update_unit_options()

    # 单位转换功能实现（简单函数）
    def update_unit_options(self):
        conversion_type = self.conversion_type.get()

        if conversion_type == "长度":
            units = ["米", "厘米", "毫米", "千米", "英寸", "英尺", "码", "英里"]
        elif conversion_type == "重量":
            units = ["千克", "克", "毫克", "吨", "磅", "盎司"]
        elif conversion_type == "温度":
            units = ["摄氏度", "华氏度", "开尔文"]
        elif conversion_type == "面积":
            units = ["平方米", "平方厘米", "平方毫米", "公顷", "亩", "平方英尺", "平方英寸"]

        self.from_unit['values'] = units
        self.to_unit['values'] = units
        if units:
            self.from_unit.current(0)
            self.to_unit.current(1)
        self.status_bar.config(text=f"已选择{conversion_type}转换")

    def convert_units(self):
        try:
            value = float(self.conversion_value.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()
            conversion_type = self.conversion_type.get()

            if conversion_type == "长度":
                result = self.convert_length(value, from_unit, to_unit)
            elif conversion_type == "重量":
                result = self.convert_weight(value, from_unit, to_unit)
            elif conversion_type == "温度":
                result = self.convert_temperature(value, from_unit, to_unit)
            elif conversion_type == "面积":
                result = self.convert_area(value, from_unit, to_unit)

            self.conversion_result.set(f"{value} {from_unit} = {result:.6f} {to_unit}")
            self.status_bar.config(text="单位转换完成")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数值")
            self.status_bar.config(text="单位转换失败")
        except Exception as e:
            messagebox.showerror("错误", str(e))
            self.status_bar.config(text="单位转换失败")

    def convert_length(self, value, from_unit, to_unit):
        # 转换为米作为中间单位
        to_meter = {
            "米": 1,
            "厘米": 0.01,
            "毫米": 0.001,
            "千米": 1000,
            "英寸": 0.0254,
            "英尺": 0.3048,
            "码": 0.9144,
            "英里": 1609.34
        }
        return value * to_meter[from_unit] / to_meter[to_unit]

    def convert_weight(self, value, from_unit, to_unit):
        # 转换为千克作为中间单位
        to_kg = {
            "千克": 1,
            "克": 0.001,
            "毫克": 0.000001,
            "吨": 1000,
            "磅": 0.453592,
            "盎司": 0.0283495
        }
        return value * to_kg[from_unit] / to_kg[to_unit]

    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        # 先转换为摄氏度作为中间单位
        if from_unit == "摄氏度":
            celsius = value
        elif from_unit == "华氏度":
            celsius = (value - 32) * 5 / 9
        elif from_unit == "开尔文":
            celsius = value - 273.15

        # 转换为目标单位
        if to_unit == "摄氏度":
            return celsius
        elif to_unit == "华氏度":
            return celsius * 9 / 5 + 32
        elif to_unit == "开尔文":
            return celsius + 273.15

    def convert_area(self, value, from_unit, to_unit):
        # 转换为平方米作为中间单位
        to_sqm = {
            "平方米": 1,
            "平方厘米": 0.0001,
            "平方毫米": 0.000001,
            "公顷": 10000,
            "亩": 666.6667,
            "平方英尺": 0.092903,
            "平方英寸": 0.00064516
        }
        return value * to_sqm[from_unit] / to_sqm[to_unit]

    # ------------------------------
    # 密码生成器标签页
    # ------------------------------
    def create_password_generator_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="密码生成器")

        # 设置区域
        settings_frame = ttk.LabelFrame(tab, text="密码设置")
        settings_frame.pack(fill=tk.X, padx=10, pady=5)

        # 密码长度
        ttk.Label(settings_frame, text="密码长度:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.password_length = tk.IntVar(value=12)
        ttk.Scale(settings_frame, from_=6, to=32, variable=self.password_length,
                  command=lambda v: self.update_length_label(v)).grid(row=0, column=1, padx=5, pady=5)
        self.length_label = ttk.Label(settings_frame, text="12")
        self.length_label.grid(row=0, column=2, padx=5, pady=5)

        # 密码选项
        self.include_uppercase = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings_frame, text="包含大写字母 (A-Z)", variable=self.include_uppercase).grid(
            row=1, column=0, columnspan=3, sticky=tk.W, padx=5, pady=2)

        self.include_lowercase = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings_frame, text="包含小写字母 (a-z)", variable=self.include_lowercase).grid(
            row=2, column=0, columnspan=3, sticky=tk.W, padx=5, pady=2)

        self.include_numbers = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings_frame, text="包含数字 (0-9)", variable=self.include_numbers).grid(
            row=3, column=0, columnspan=3, sticky=tk.W, padx=5, pady=2)

        self.include_symbols = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings_frame, text="包含特殊字符 (!@#$等)", variable=self.include_symbols).grid(
            row=4, column=0, columnspan=3, sticky=tk.W, padx=5, pady=2)

        # 按钮
        button_frame = ttk.Frame(tab)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(button_frame, text="生成密码", command=self.generate_password).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="复制密码", command=self.copy_password).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="生成10个密码", command=self.generate_multiple_passwords).pack(side=tk.LEFT,
                                                                                                     padx=5)

        # 结果区域
        result_frame = ttk.LabelFrame(tab, text="生成的密码")
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.generated_password = tk.StringVar()
        ttk.Entry(result_frame, textvariable=self.generated_password, font=("Microsoft YaHei", 12),
                  state="readonly").pack(fill=tk.X, padx=5, pady=5)

        self.password_list = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, height=6)
        self.password_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # 密码生成器功能实现（简单函数）
    def update_length_label(self, value):
        self.length_label.config(text=str(int(float(value))))
        self.status_bar.config(text=f"密码长度设置为: {int(float(value))}")

    def generate_password(self):
        length = self.password_length.get()

        # 确保至少选择了一种字符类型
        if not (self.include_uppercase.get() or self.include_lowercase.get() or
                self.include_numbers.get() or self.include_symbols.get()):
            messagebox.showerror("错误", "请至少选择一种字符类型")
            return

        # 构建字符集
        chars = ""
        if self.include_uppercase.get():
            chars += string.ascii_uppercase
        if self.include_lowercase.get():
            chars += string.ascii_lowercase
        if self.include_numbers.get():
            chars += string.digits
        if self.include_symbols.get():
            chars += string.punctuation

        # 生成密码
        password = ''.join(random.choice(chars) for _ in range(length))
        self.generated_password.set(password)
        self.status_bar.config(text="已生成密码")

    def generate_multiple_passwords(self):
        self.password_list.delete("1.0", tk.END)
        for i in range(10):
            self.generate_password()
            self.password_list.insert(tk.END, f"{i + 1}. {self.generated_password.get()}\n")
        self.status_bar.config(text="已生成10个密码")

    def copy_password(self):
        password = self.generated_password.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("提示", "密码已复制到剪贴板")
            self.status_bar.config(text="已复制密码到剪贴板")

    # ------------------------------
    # 日期时间工具标签页
    # ------------------------------
    def create_datetime_tool_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="日期时间工具")

        # 当前时间显示
        current_time_frame = ttk.LabelFrame(tab, text="当前时间")
        current_time_frame.pack(fill=tk.X, padx=10, pady=5)

        self.current_datetime = tk.StringVar()
        ttk.Label(current_time_frame, textvariable=self.current_datetime, font=("Microsoft YaHei", 12)).pack(
            padx=5, pady=5, anchor=tk.W)
        self.update_current_time()

        # 日期计算
        date_calc_frame = ttk.LabelFrame(tab, text="日期计算")
        date_calc_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(date_calc_frame, text="基准日期 (YYYY-MM-DD):").grid(
            row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.base_date = ttk.Entry(date_calc_frame, width=15)
        self.base_date.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(date_calc_frame, text="使用今天", command=self.use_today).grid(
            row=0, column=2, padx=5, pady=5)

        ttk.Label(date_calc_frame, text="天数:").grid(
            row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.days_to_add = ttk.Entry(date_calc_frame, width=10)
        self.days_to_add.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(date_calc_frame, text="(正数表示未来，负数表示过去)").grid(
            row=1, column=2, padx=5, pady=5, sticky=tk.W)

        ttk.Button(date_calc_frame, text="计算日期", command=self.calculate_date).grid(
            row=2, column=0, padx=5, pady=5)

        # 结果
        self.date_result = tk.StringVar()
        ttk.Label(date_calc_frame, textvariable=self.date_result).grid(
            row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)

        # 时间差计算
        date_diff_frame = ttk.LabelFrame(tab, text="日期差计算")
        date_diff_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(date_diff_frame, text="开始日期 (YYYY-MM-DD):").grid(
            row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.start_date = ttk.Entry(date_diff_frame, width=15)
        self.start_date.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(date_diff_frame, text="结束日期 (YYYY-MM-DD):").grid(
            row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.end_date = ttk.Entry(date_diff_frame, width=15)
        self.end_date.grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(date_diff_frame, text="计算差值", command=self.calculate_date_diff).grid(
            row=1, column=0, padx=5, pady=5)

        self.date_diff_result = tk.StringVar()
        ttk.Label(date_diff_frame, textvariable=self.date_diff_result).grid(
            row=1, column=1, columnspan=3, padx=5, pady=5, sticky=tk.W)

    # 日期时间工具功能实现（简单函数）
    def update_current_time(self):
        now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
        self.current_datetime.set(now)
        self.root.after(1000, self.update_current_time)  # 每秒更新一次

    def use_today(self):
        today = datetime.now().strftime("%Y-%m-%d")
        self.base_date.delete(0, tk.END)
        self.base_date.insert(0, today)
        self.status_bar.config(text="已设置基准日期为今天")

    def calculate_date(self):
        try:
            base_date_str = self.base_date.get()
            days = int(self.days_to_add.get())

            base_date = datetime.strptime(base_date_str, "%Y-%m-%d")
            result_date = base_date + timedelta(days=days)

            weekday_map = ["一", "二", "三", "四", "五", "六", "日"]
            self.date_result.set(
                f"计算结果: {result_date.strftime('%Y年%m月%d日')} (星期{weekday_map[result_date.weekday()]})"
            )
            self.status_bar.config(text="日期计算完成")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的日期和天数")
            self.status_bar.config(text="日期计算失败")

    def calculate_date_diff(self):
        try:
            start_date_str = self.start_date.get()
            end_date_str = self.end_date.get()

            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

            diff = end_date - start_date
            years = diff.days // 365
            months = (diff.days % 365) // 30
            days = (diff.days % 365) % 30

            self.date_diff_result.set(
                f"两个日期相差: {diff.days} 天 ({years}年{months}月{days}天)"
            )
            self.status_bar.config(text="日期差计算完成")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的日期")
            self.status_bar.config(text="日期差计算失败")

    # ------------------------------
    # 文本分析工具标签页
    # ------------------------------
    def create_text_analyzer_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="文本分析")

        # 输入区域
        input_frame = ttk.LabelFrame(tab, text="输入文本")
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5, side=tk.LEFT)

        self.analyzer_input = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, width=40, height=20)
        self.analyzer_input.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        ttk.Button(input_frame, text="分析文本", command=self.analyze_text).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(input_frame, text="清除", command=self.clear_analyzer).pack(fill=tk.X, padx=5, pady=5)

        # 结果区域
        result_frame = ttk.LabelFrame(tab, text="分析结果")
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5, side=tk.RIGHT)

        self.analyzer_result = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, width=40, height=20,
                                                         state="disabled")
        self.analyzer_result.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # 文本分析功能实现（简单函数）
    def analyze_text(self):
        text = self.analyzer_input.get("1.0", tk.END).rstrip()
        if not text:
            messagebox.showinfo("提示", "请输入要分析的文本")
            return

        # 基本统计
        char_count = len(text)
        char_count_no_space = len(text.replace(" ", ""))
        word_count = len(text.split())
        line_count = text.count('\n') + 1 if text else 0

        # 字母统计
        letters = sum(c.isalpha() for c in text)
        uppercase = sum(c.isupper() for c in text)
        lowercase = sum(c.islower() for c in text)

        # 数字统计
        digits = sum(c.isdigit() for c in text)

        # 特殊字符统计
        special_chars = char_count - letters - digits - sum(c.isspace() for c in text)

        # 提取邮箱（简单匹配）
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

        # 提取网址（简单匹配）
        urls = re.findall(r'https?://\S+|www\.\S+', text)

        # 构建结果
        result = []
        result.append(f"基本统计:")
        result.append(f"  总字符数: {char_count} (不含空格: {char_count_no_space})")
        result.append(f"  单词数: {word_count}")
        result.append(f"  行数: {line_count}")
        result.append("\n字符类型统计:")
        result.append(f"  字母: {letters} (大写: {uppercase}, 小写: {lowercase})")
        result.append(f"  数字: {digits}")
        result.append(f"  特殊字符: {special_chars}")

        if emails:
            result.append(f"\n发现邮箱 ({len(emails)}):")
            for email in emails[:3]:  # 只显示前3个
                result.append(f"  - {email}")
            if len(emails) > 3:
                result.append(f"  ... 还有 {len(emails) - 3} 个邮箱")

        if urls:
            result.append(f"\n发现网址 ({len(urls)}):")
            for url in urls[:3]:  # 只显示前3个
                result.append(f"  - {url}")
            if len(urls) > 3:
                result.append(f"  ... 还有 {len(urls) - 3} 个网址")

        # 显示结果
        self.analyzer_result.config(state="normal")
        self.analyzer_result.delete("1.0", tk.END)
        self.analyzer_result.insert(tk.END, '\n'.join(result))
        self.analyzer_result.config(state="disabled")
        self.status_bar.config(text="文本分析完成")

    def clear_analyzer(self):
        self.analyzer_input.delete("1.0", tk.END)
        self.analyzer_result.config(state="normal")
        self.analyzer_result.delete("1.0", tk.END)
        self.analyzer_result.config(state="disabled")
        self.status_bar.config(text="已清除分析文本")


if __name__ == "__main__":
    root = tk.Tk()
    app = UtilityToolkit(root)
    root.mainloop()
