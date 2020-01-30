import QtQuick.Layouts 1.14
import QtQuick 2.14

ColumnLayout{
    property bool touche: num % 5
    property bool navire: false
    property int num

    Layout.fillWidth : true
    
    Rectangle {
        id : rect
        height : 35
        width : 35
        color : (navire || mouseA.containsMouse) ? "#54647d" : "white"
        border.width : 1
        opacity : mouseA.containsMouse ? 0.5 : 1

        Image{
            id : img
            source : navire ? "../Images/cross.png" : "../Images/close.png"
            width : navire ? (parent.width * 0.85) : (parent.width * 0.65)
            height : width
            anchors.centerIn: parent
            opacity : touche

            Behavior on opacity{
                NumberAnimation{
                    duration : 420
                }
            }
            
        }
        MouseArea{
            id : mouseA
            anchors.fill : parent
            acceptedButtons: Qt.LeftButton | Qt.RightButton
            hoverEnabled : true
            onClicked:{
                if(mouse.button == Qt.LeftButton){
                     navire = !navire                   
                }
                if(mouse.button  == Qt.RightButton){
                    touche = !touche
                }
                console.log(num)
            }
        }
    }
}