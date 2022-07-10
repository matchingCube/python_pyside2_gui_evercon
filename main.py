from screen import *
from incoming_call import *
from Custom_Widgets.Widgets import *
import pickle

vol_x_icon = QIcon()
vol_x_icon.addFile(":/icons/icons/volume-x.svg")
music_icon = QIcon()
music_icon.addFile(":/icons/icons/music.svg")


extension = input("Please input extension: ")


def change_vol_icon(button, volume_val):
    vol_icon = QIcon()
    if volume_val > 70:
        vol_icon.addFile(":/icons/icons/volume-2.svg")
        button.setIcon(vol_icon)
    elif 30 < volume_val < 71:
        vol_icon.addFile(":/icons/icons/volume-1.svg")
        button.setIcon(vol_icon)
    elif 0 < volume_val < 31:
        vol_icon.addFile(":/icons/icons/volume.svg")
        button.setIcon(vol_icon)
    elif volume_val == 0:
        button.setIcon(vol_x_icon)


def get_txt_content(path):
    if not os.path.exists(path):
        f = open(path, "w+")
        f.close()
    txt_file = open(path, "r")
    txt_content = txt_file.read()
    txt_file.close()
    return txt_content


class IncomingCall(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.parent = parent
        self.ui = Ui_IncomingScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # set notification text
        self.ui.informLabel.setText("Incoming Call from Extension #" + extension)
        # set gif as background
        self.movie = QMovie(":/images/images/incoming_call_2.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()
        # signal
        self.ui.acceptBtn.clicked.connect(self.acceptAction)
        self.ui.discardBtn.clicked.connect(self.discardAction)

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def acceptAction(self):
        print("Accept Button was clicked")
        self.close()

    def discardAction(self):
        print("Discard Button was clicked")
        self.close()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.curPath = os.getcwd()
        self.recorded_path = self.curPath + "/Recorded"
        self.profile_path = self.curPath + "/content/profile.txt"
        self.help_path = self.curPath + "/content/help.txt"
        self.noti_content_list = ["Welcome to EVERCON.",
                                  "No audio is selected. Please select one.",
                                  "No field station is selected. Please select one.",
                                  "No zone is selected. Please select one."]
        self.schedules = []
        self.zonesIP = {
            "Lobby Area": "244.0.0.1",
            "PANTRY": "244.0.4.13",
            "Accounts Section": "244.10.1.1",
            "Main Office": "244.0.10.13",
            "Gate 1": "244.5.45.10",
            "Gate 2": "244.10.30.17"
        }
        self.popup_window = None

        # add Json Stylesheet to app
        loadJsonStyle(self, self.ui)

        # set Data and Time in footer
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

        # check whether matching schedule exists
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.start_one_min_timer)
        self.timer.start()

        self.check_timer = QTimer(self)
        self.check_timer.setInterval(60000)
        self.check_timer.timeout.connect(self.check_schedule)

        # Set Profile Content
        profile_content = get_txt_content(self.profile_path)
        self.ui.profile_content.setText(profile_content)

        # Help Profile Content
        help_content = get_txt_content(self.help_path)
        self.ui.help_content.setText(help_content)

        # change weekend color
        saturday_format = self.ui.calendarWidget.weekdayTextFormat(Qt.Saturday)
        saturday_format.setForeground(QBrush(QColor(200, 80, 112), Qt.SolidPattern))
        self.ui.calendarWidget.setWeekdayTextFormat(Qt.Saturday, saturday_format)
        sunday_format = self.ui.calendarWidget.weekdayTextFormat(Qt.Sunday)
        sunday_format.setForeground(QBrush(QColor(255, 70, 110), Qt.SolidPattern))
        self.ui.calendarWidget.setWeekdayTextFormat(Qt.Sunday, sunday_format)

        # Set List of Select Audio
        if not os.path.exists(self.recorded_path):
            os.mkdir(self.recorded_path)
        file_list = os.listdir(self.recorded_path)
        for file_name in file_list:
            recorded_audio_item = QListWidgetItem(music_icon, file_name)
            self.ui.listRecordedAudio.addItem(recorded_audio_item)
            recorded_audio_item = QListWidgetItem(music_icon, file_name)
            self.ui.listRecordedAudio_2.addItem(recorded_audio_item)
            recorded_audio_item = QListWidgetItem(music_icon, file_name)
            self.ui.listRecordedAudio_3.addItem(recorded_audio_item)

        # Set List of Schedules
        if os.path.exists('schedules.pkl'):
            with open('schedules.pkl', 'rb') as file:
                self.schedules = pickle.load(file)
            print("####### Schedule List was loaded successfully! #######")
            print(self.schedules, '\n')
        for schedule_item in self.schedules:
            schedule_audio_item = QListWidgetItem(music_icon, schedule_item["audio"])
            self.ui.listSchedule.addItem(schedule_audio_item)

        # Signal and Slot
        # Show Center Menu
        self.ui.btnSettings.clicked.connect(lambda: self.ui.center_menu.expandMenu())
        self.ui.btnSettings.clicked.connect(lambda: self.ui.moreMenuLabel.setText("Settings"))
        self.ui.btnInfo.clicked.connect(lambda: self.ui.center_menu.expandMenu())
        self.ui.btnInfo.clicked.connect(lambda: self.ui.moreMenuLabel.setText("Information"))
        self.ui.btnHelp.clicked.connect(lambda: self.ui.center_menu.expandMenu())
        self.ui.btnHelp.clicked.connect(lambda: self.ui.moreMenuLabel.setText("Help"))

        # Close Center Menu
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.center_menu.collapseMenu())

        # Show Right Menu
        self.ui.btnProfile.clicked.connect(lambda: self.ui.right_menu_container.expandMenu())
        self.ui.btnProfile.clicked.connect(lambda: self.ui.rightMenuLabel.setText("Profile"))
        self.ui.btnMore.clicked.connect(lambda: self.ui.right_menu_container.expandMenu())
        self.ui.btnMore.clicked.connect(lambda: self.ui.rightMenuLabel.setText("More"))

        # Close Right Menu
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.right_menu_container.collapseMenu())

        # Show Notification
        self.ui.btnNotification.clicked.connect(lambda: self.ui.notification_content.setText(self.noti_content_list[0]))

        # Close Notification
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popup_notification_container.collapseMenu())

        # Adapt for Volume Slider Change
        self.ui.volumeSlider.valueChanged.connect(self.adapt_volume)
        self.ui.volumeSlider_2.valueChanged.connect(self.adapt_volume_2)
        self.ui.volumeSlider_3.valueChanged.connect(self.adapt_volume_3)

        # Mute Volume on Click Volume Button
        self.ui.btnVolume.clicked.connect(self.control_volume_mute)
        self.ui.btnVolume_2.clicked.connect(self.control_volume_mute_2)
        self.ui.btnVolume_3.clicked.connect(self.control_volume_mute_3)

        # Add Schedule to the List of Schedules
        self.ui.btnAddToSchedule.clicked.connect(self.add_schedule)

        # Start Field Station
        self.ui.btnStartInField.clicked.connect(self.start_field)

        # Start Zones
        self.ui.btnStart.clicked.connect(self.start_zones)

        # Call Incoming Screen
        self.ui.btnReports.clicked.connect(self.call_incoming)
        self.ui.btnDataAnalysis.clicked.connect(self.call_incoming)

    def call_incoming(self):
        if self.popup_window is None:
            self.popup_window = IncomingCall()
            self.popup_window.show()
        else:
            self.popup_window.close()
            self.popup_window = None

    def start_one_min_timer(self):
        if QTime.currentTime().second() == 0:
            print("Found 0 second point! Now a minute timer is started!\n")
            self.timer.stop()
            self.timer.deleteLater()
            self.check_timer.start()
            self.check_schedule()

    def check_schedule(self):
        curTime = QTime.currentTime()
        curMin = curTime.minute()
        curHour = curTime.hour()
        curDate = QDate.currentDate()
        curYear = curDate.year()
        curMonth = curDate.month()
        curDay = curDate.day()
        for schedule_item in self.schedules:
            if schedule_item['date']['year'] == curYear and \
               schedule_item['date']['month'] == curMonth and \
               schedule_item['date']['day'] == curDay and \
               schedule_item['time']['hour'] == curHour and \
               schedule_item['time']['minute'] == curMin:
                print('A matching schedule exists!')
                print(f'{curDay}/{curMonth}/{curYear} {curHour}:{curMin}\n')
                break

    def start_zones(self):
        checked_zones = []
        if self.ui.lobbyCheck.isChecked():
            zoneName = self.ui.lobbyLabel.text()
            checked_zones.append([zoneName, self.zonesIP[zoneName]])
        if self.ui.pantryCheck.isChecked():
            zoneName = self.ui.pantryLabel.text()
            checked_zones.append([zoneName, self.zonesIP[zoneName]])
        if self.ui.accountsCheck.isChecked():
            zoneName = self.ui.accountsLabel.text()
            checked_zones.append([zoneName, self.zonesIP[zoneName]])
        if self.ui.mainOfficeCheck.isChecked():
            zoneName = self.ui.mainOfficeLabel.text()
            checked_zones.append([zoneName, self.zonesIP[zoneName]])
        if self.ui.gate1Check.isChecked():
            zoneName = self.ui.gate1Label.text()
            checked_zones.append([zoneName, self.zonesIP[zoneName]])
        if self.ui.gate2Check.isChecked():
            zoneName = self.ui.gate2Label.text()
            checked_zones.append([zoneName, self.zonesIP[zoneName]])
        if len(checked_zones) == 0:
            self.ui.notification_content.setText(self.noti_content_list[3])
            self.ui.popup_notification_container.expandMenu()
        elif self.ui.radioRecorded.isChecked() and len(self.ui.listRecordedAudio.selectedItems()) == 0:
            self.ui.notification_content.setText(self.noti_content_list[1])
            self.ui.popup_notification_container.expandMenu()
        else:
            audio_name = ""
            if self.ui.radioRecorded.isChecked():
                audio_name = self.ui.listRecordedAudio.currentItem().text()
            selected_zone_info = {
                "zones": checked_zones,
                "audio": audio_name,
                "volumeLevel": self.ui.volumeSlider.value()
            }
            printZonesList = ""
            for index, item in enumerate(checked_zones):
                if index == len(checked_zones) - 1:
                    printZonesList += f"'{item[0]}'."
                else:
                    printZonesList += f"'{item[0]}', "
            if selected_zone_info['audio'] == "":
                print("Playing from Mic on ZONE " + printZonesList + '\n')
            else:
                print("Playing a Recorded message '" + audio_name + "' on ZONE " + printZonesList + '\n')
            print("Here is current zones information.")
            print(selected_zone_info, '\n')

    def start_field(self):
        if len(self.ui.listField.selectedItems()) == 0:
            self.ui.notification_content.setText(self.noti_content_list[2])
            self.ui.popup_notification_container.expandMenu()
        elif self.ui.radioRecordedInField.isChecked() and len(self.ui.listRecordedAudio_3.selectedItems()) == 0:
            self.ui.notification_content.setText(self.noti_content_list[1])
            self.ui.popup_notification_container.expandMenu()
        else:
            field_text = self.ui.listField.currentItem().text()
            ipExtList = field_text.split()
            audio_name = ""
            if self.ui.radioRecordedInField.isChecked():
                audio_name = self.ui.listRecordedAudio_3.currentItem().text()
            field_info = {
                "playMode": "mic" if self.ui.radioMicInField.isChecked() else "recorded",
                "ipExt": ipExtList,
                "volumeLevel": self.ui.volumeSlider_3.value(),
                "audio": audio_name
            }
            print("####### A Field Station was started #######")
            print(field_info, '\n')

    def add_schedule(self):
        if len(self.ui.listRecordedAudio_2.selectedItems()) == 0:
            self.ui.notification_content.setText(self.noti_content_list[1])
            self.ui.popup_notification_container.expandMenu()
        else:
            selected_date = self.ui.calendarWidget.selectedDate()
            schedule_date = {
                "year": selected_date.year(),
                "month": selected_date.month(),
                "day": selected_date.day()
            }
            selected_time = self.ui.timeEdit.time()
            schedule_time = {
                "hour": selected_time.hour(),
                "minute": selected_time.minute()
            }
            audio_name = self.ui.listRecordedAudio_2.currentItem().text()
            newSchedule = {
                "date": schedule_date,
                "time": schedule_time,
                "isEveryday": self.ui.checkEveryday.isChecked(),
                "audio": audio_name,
                "volumeLevel": self.ui.volumeSlider_2.value()
            }

            new_item = QListWidgetItem(music_icon, audio_name)
            self.ui.listSchedule.addItem(new_item)
            self.schedules.append(newSchedule)
            print("####### New Schedule was added to Schedule List #######")
            print(newSchedule, '\n')

            # Save Schedule List as Pickle File
            with open('schedules.pkl', 'wb') as file:
                pickle.dump(self.schedules, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("####### Schedule List was saved successfully! #######")
            print(self.schedules, '\n')

    def adapt_volume(self):
        current_val = self.ui.volumeSlider.value()
        self.ui.labelVolume.setText(str(current_val))
        change_vol_icon(self.ui.btnVolume, current_val)

    def adapt_volume_2(self):
        current_val = self.ui.volumeSlider_2.value()
        self.ui.labelVolume_2.setText(str(current_val))
        change_vol_icon(self.ui.btnVolume_2, current_val)

    def adapt_volume_3(self):
        current_val = self.ui.volumeSlider_3.value()
        self.ui.labelVolume_3.setText(str(current_val))
        change_vol_icon(self.ui.btnVolume_3, current_val)

    def control_volume_mute(self):
        if self.ui.btnVolume.isChecked():
            self.ui.btnVolume.setIcon(vol_x_icon)
            self.ui.volumeSlider.setDisabled(True)
        else:
            self.ui.volumeSlider.setDisabled(False)
            change_vol_icon(self.ui.btnVolume, self.ui.volumeSlider.value())

    def control_volume_mute_2(self):
        if self.ui.btnVolume_2.isChecked():
            self.ui.btnVolume_2.setIcon(vol_x_icon)
            self.ui.volumeSlider_2.setDisabled(True)
        else:
            self.ui.volumeSlider_2.setDisabled(False)
            change_vol_icon(self.ui.btnVolume_2, self.ui.volumeSlider_2.value())

    def control_volume_mute_3(self):
        if self.ui.btnVolume_3.isChecked():
            self.ui.btnVolume_3.setIcon(vol_x_icon)
            self.ui.volumeSlider_3.setDisabled(True)
        else:
            self.ui.volumeSlider_3.setDisabled(False)
            change_vol_icon(self.ui.btnVolume_3, self.ui.volumeSlider_3.value())

    def showtime(self):
        DateTime = QDateTime.currentDateTime()
        date_str = DateTime.toString("dd/MM/yyyy")
        time_str = DateTime.toString("hh:mm:ss AP")
        self.ui.dateShowLabel.setText(date_str)
        self.ui.timeShowLabel.setText(time_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
