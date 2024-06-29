import flet as ft

def main(page: ft.Page):
    page.title = "svg2pdf"
    page.window.height = 600
    page.window.width = 800

    dir_path_default_text = r"保存先ディレクトリを選択してください"
    dir_path_field = ft.TextField(label="保存先ディレクトリ", disabled=True, value=dir_path_default_text)

    def on_dialog_select_path_result(e: ft.FilePickerResultEvent):
        dir_path_field.value = e.path
        page.update()

    file_picker = ft.FilePicker(on_result=on_dialog_select_path_result)

    page.overlay.append(file_picker)
    page.update()

    dir_picker = ft.ElevatedButton("ディレクトリを選択...",
        on_click=lambda _: file_picker.get_directory_path(),
        col={"sm": 4, "md": 4, "xl": 4})

    path_field_row = ft.ResponsiveRow([dir_path_field])
    dir_picker_row = ft.ResponsiveRow([dir_picker], alignment=ft.MainAxisAlignment.END)

    page.add(path_field_row, dir_picker_row)

    # def add_clicked(e):
    #     page.add(ft.Checkbox(label=new_task.value, on_change=checked))
    #     new_task.value = ""
    #     new_task.focus()
    #     new_task.update()

    # def checked(e):
    #     print("checked")
    #     # print(dir(e.control.label_style))
    #     e.control.label_style = ft.Text(italic=True)

    # def on_dialog_result(e: ft.FilePickerResultEvent):
    #     print("this is path")

    # file_picker = ft.FilePicker(on_result=on_dialog_result)

    # new_task = ft.TextField(hint_text="what is this", width=300)
    # # picker = ft.FilePicker()

    # dir_picker = ft.ElevatedButton("Choose dir...",
    #     on_click=lambda _: file_picker.get_directory_path())

    # page.overlay.append(file_picker)
    # page.update()

    # page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked), dir_picker]))

ft.app(target=main)
