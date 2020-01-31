import QtQuick 2.6
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14
import QtQuick.Window 2.14

import "Attaque"
import "Defense"

ApplicationWindow {
    visible: true
    
    minimumWidth : mainLayout.implicitWidth
    minimumHeight : mainLayout.implicitHeight

    RowLayout{
        id : mainLayout
        Layout.margins : 20
        anchors.fill : parent
        spacing : 10
        RowLayout{}
        CarteAttaque{
            id : attaq
        }
        RowLayout{}

        ToolSeparator {
            Layout.fillHeight : true
            Layout.maximumHeight : attaq.implicitHeight + 40
        }
        RowLayout{}

        CarteDefense{
            id : carteDef
            focus : true
        }

        RowLayout{}           
    }           
}