import QtQuick 2.6
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14

ColumnLayout{
    ColumnLayout{}
    PageIndicator {
        Layout.alignment : Qt.AlignHCenter
        currentIndex: stacklayout.currentIndex
        count: stacklayout.count
    }
    StackLayout {
        Layout.leftMargin : 20
        Layout.rightMargin : 20
        Layout.bottomMargin : 20
        id : stacklayout
        Repeater{
            model : 3
            GridLayout {
                id : defGrid
                rowSpacing : 0
                columnSpacing : 0
                columns : 15
                Repeater{
                    model : 225
                    CaseDef {
                        num : index
                    }
                }
            }
        }
    }
    Keys.onPressed: {
        if (event.key == Qt.Key_1 || event.key == 38) {
            stacklayout.currentIndex = 0
            event.accepted = true;
        }
        else if (event.key == Qt.Key_2 || event.key == 201) {
            event.accepted = true;
            stacklayout.currentIndex = 1
        }
        else if (event.key == Qt.Key_3 || event.key == 34) {
            stacklayout.currentIndex = 2
            event.accepted = true;
        }
        console.log(stacklayout.currentIndex)
    }
}