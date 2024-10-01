from argparse import FileType
from tkinter import Tk
from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
from tkinter import filedialog
import flet as ft
import os

root = Tk()

mixer.init()
test1 = open("test.txt","r+")
print(test1)

def main(page: ft.Page):
    page.title = "Music Player"

    cd = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("Music Title"),
                        subtitle=ft.Text(
                            "Music Subtitle"
                        ),
                    ),
                    ft.Row(
                        [ft.TextButton("Play" , on_click=""), ft.TextButton("Stop")],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

    class Example(ft.Row):
        def __init__(self):
            super().__init__()
            self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
            self.selected_files = ft.Text()

            def pick_files(_):
                self.pick_files_dialog.pick_files(allow_multiple=False , file_type= "mp3")

            self.controls = [
                ft.ElevatedButton(
                    "Pick music",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=pick_files,
                ),
                self.selected_files,
            ]

        def pick_files_result(self, e: ft.FilePickerResultEvent):
            self.selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
            )
            self.selected_files.update()

        # happens when example is added to the page (when user chooses the FilePicker control from the grid)
        def did_mount(self):
            self.page.overlay.append(self.pick_files_dialog)
            self.page.update()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        def will_unmount(self):
            self.page.overlay.remove(self.pick_files_dialog)
            self.page.update()

    filepicker_example = Example()
    """
    def play(name):
        mixer.music.load(name)
        print(name)
        mixer.music.play()
        pb.start

    def stop():
        mixer.music.pause()
    """
    """
    def select():
        directory = os.getcwd()
        filename = filedialog.askopenfilename(initialdir= directory, title="Select a File",filetypes=(("Music files", "*.mp3 .wav*"), ("all files", "*.*")),initialfile = "Untitled")
        play(filename)
        file = open("test.txt","w+")
        file.write(filename)
        file.close()
    pb = Progressbar(root, orient='horizontal', mode='indeterminate',length=28)
    pb.pack()
    """
    """
    def resume():
        mil = (mixer.music.get_pos() / 1000)
        seconds = int(mil)
        print(seconds)
        pb['value'] += seconds
        mixer.music.unpause()
    """
    page.add(cd)
    page.add(filepicker_example)
ft.app(main)
