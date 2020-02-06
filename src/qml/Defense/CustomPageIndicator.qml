import QtQuick 2.6
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14

ColumnLayout {
    id: indicator
    property int currentIndex: 0
    property int count: 0

    Layout.alignment: Qt.AlignVCenter

    Repeater{
        model : indicator.count
        ColumnLayout{
            property bool isCurrentIndex: index === indicator.currentIndex

            Rectangle {
                id : rect

                Layout.alignment: Qt.AlignHCenter
                implicitWidth: 8
                implicitHeight: isCurrentIndex ? 165 : 50
                radius: height / 2
                color: isCurrentIndex ? "#1303fc" : "#8597ab"
                opacity: isCurrentIndex ? 0.95 : 0.45
                Behavior on implicitHeight {
                    NumberAnimation {
                        duration: 223
                    }
                }
            }
        }
    }
}