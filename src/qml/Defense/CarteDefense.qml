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
}