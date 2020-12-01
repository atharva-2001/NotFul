from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Demo notification",
                   "Hello world",
                   duration=10)