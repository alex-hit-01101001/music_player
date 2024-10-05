from pygame import mixer
import flet as ft
import time
import threading
import os

# Initialize the mixer for pygame
mixer.init()


def main(page: ft.Page):
    page.title = "Music Player"

    # Progress bar to indicate music playback
    progress_bar = ft.ProgressBar(width=400, value=0)

    # Centered layout
    container = ft.Container(
        content=ft.Column(
            [
                ft.ListTile(
                    leading=ft.Icon(ft.icons.ALBUM),
                    title=ft.Text("Music Title"),
                    subtitle=ft.Text("Music Subtitle"),
                ),
                ft.Row(
                    [
                        ft.TextButton("Play", on_click=lambda e: play_music(progress_bar)),
                        ft.TextButton("Stop", on_click=lambda e: stop_music(progress_bar)),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                progress_bar,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        width=400,
        padding=10,
    )

    cd = ft.Card(content=container)

    class Example(ft.Row):
        selected_files = ft.Text()

        def __init__(self):
            super().__init__()
            self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)

            def pick_files(_):
                self.pick_files_dialog.pick_files(allow_multiple=False, file_type="mp3")

            self.controls = [
                ft.ElevatedButton(
                    "Pick music",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=pick_files,
                ),
                self.selected_files,
            ]

        def pick_files_result(self, e: ft.FilePickerResultEvent):
            if e.files:
                file_path = e.files[0].path  # Get the path of the selected file
                self.selected_files.value = file_path
                mixer.music.load(file_path)  # Load the selected file
                mixer.music.play()  # Play the loaded music
                self.selected_files.update()

                # Get the length of the audio file in seconds
                audio_length = self.get_audio_length(file_path)
                if audio_length:
                    progress_bar.max = audio_length  # Set the max of the progress bar
                    # Start the progress bar update thread
                    threading.Thread(target=self.update_progress_bar, daemon=True).start()

            else:
                self.selected_files.value = "Cancelled!"
                self.selected_files.update()

        def get_audio_length(self, file_path):
            # This function assumes the file exists and is an mp3
            if os.path.exists(file_path):
                return mixer.Sound(file_path).get_length()  # Get length in seconds
            return 0

        def update_progress_bar(self):
            while mixer.music.get_busy():
                position = mixer.music.get_pos() / 1000  # Get position in seconds
                progress_bar.value = position  # Update progress bar with the current position
                page.update()  # Update the page
                time.sleep(1)  # Update every second

        def did_mount(self):
            self.page.overlay.append(self.pick_files_dialog)
            self.page.update()

        def will_unmount(self):
            self.page.overlay.remove(self.pick_files_dialog)
            self.page.update()

    def play_music(progress_bar):
        if not mixer.music.get_busy():
            mixer.music.unpause()  # Resume playing if paused

    def stop_music(progress_bar):
        mixer.music.stop()  # Stop the music
        progress_bar.value = 0  # Reset progress bar when stopped
        progress_bar.update()

    filepicker_example = Example()

    # Center the main card in the page
    page.add(ft.Column(
        controls=[
            cd,
            filepicker_example
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    ))


ft.app(main)
