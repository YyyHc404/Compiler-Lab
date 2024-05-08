#### ctypes python内置库，调用动态链接库，操作C
- cdll 用于加载使用标准的 cdecl 调用约定导出函数的库。这意味着函数参数从右向左入栈，调用者负责清理堆栈。
- windll 用于加载使用 stdcall 调用约定导出函数的库。在 stdcall 调用约定中，函数参数也是从右向左入栈，但是由被调用者负责清理堆栈，而不是调用者。
-  oledll 也使用 stdcall 调用约定，并假定函数返回 Windows HRESULT 错误代码。 当函数调用失败时会使用错误代码自动引发 OSError 异常。
- 在 Linux 中，要求指定文件名 包括 扩展名来加载库，因此不能使用属性访问的方式来加载库。 应当使用 dll 加载器的 LoadLibrary() 
- 会同时导出同一个函数的 ANSI 版本和 UNICODE 版本。
- 有时候，dlls的导出的函数名不符合 Python 的标识符规范，比如 "??2@YAPAXI@Z"。此时，你必须使用 getattr() 方法来获得该函数。
- ctypes 使用 win32 结构化异常处理来防止由于在调用函数时使用非法参数导致的程序崩溃。

- (type * n)()语法可以创建一个包含n个type类型对象的数组