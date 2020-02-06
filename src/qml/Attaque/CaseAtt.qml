import QtQuick.Layouts 1.14
import QtQuick 2.14

ColumnLayout{
    property var touches: [0,0,0]
    property int num
    property bool manque : false

    Layout.fillWidth : true
    
    Connections {
        target : Jeu
        onTir_feedback_received:{
            touches = Jeu.get_case_attaque(num)
            manque = Jeu.get_case_manque(num)
        }
    }

    Rectangle{
        id : rect
        height : 35
        width : 35
        border.width : 1

        ColumnLayout{
            anchors.fill : parent
            spacing : 2

            Repeater{
                model : 3
                Rectangle{
                    visible : !manque
                    Layout.fillWidth : true
                    Layout.fillHeight : true
                    Layout.margins : 2
                    radius : 3
                    color : "red"
                    opacity : touches[index] == 1
                }
            }

            Image{
                id : img
                source : "../Images/close.png"
                sourceSize.width : 22
                sourceSize.height : 22
                Layout.alignment : Qt.AlignHCenter | Qt.AlignVCenter
                visible : manque
            }
        }
    }
}