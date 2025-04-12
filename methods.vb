Declare PtrSafe Function GetCursorPos Lib "user32" (p As Ponteiro) As Long
Declare PtrSafe Function SetCursorPos Lib "user32" (ByVal x As Long, ByVal y As Long) As Long
Declare PtrSafe Sub mouse_event Lib "user32" (ByVal dwFlags As Long, ByVal dx As Long, ByVal dy As Long, ByVal cButtons As Long, ByVal dwExtraInfo As Long)

Type Ponteiro
   xPos As Long
   yPos As Long
End Type

Function TimeString(t As Long) As String
    Dim h As Long, m As Long, s As Long
    h = t \ 3600
    m = (t - h * 3600) \ 60
    s = Round(t - h * 3600 - m * 60, 0)
    TimeString = WorksheetFunction.Text(h, "0") & ":" & WorksheetFunction.Text(m, "00") & ":" & WorksheetFunction.Text(s, "00")
End Function

Sub WaitPlease(t As Long)
    Application.Wait (Now + TimeValue(TimeString(t)))
End Sub

Sub SetLoop()
    Dim i As Integer, t As Long
    i = 1
    t = 3
    ThisWorkbook.Sheets("home").Range("A1").Select
    While True
        WaitPlease t
        ActiveCell.Offset(0, i).Select
        i = i * (-1)
'        ActiveCell.Value = GetCursorPos
    Wend
End Sub

Sub MovingLoop()
    Dim p As Ponteiro, i As Integer, t As Long
    i = 1
    t = 15
    While True
        WaitPlease t
        GetCursorPos p
        SetCursorPos p.xPos + 30 * i, p.yPos
        Call mouse_event(&H2, 0, 0, 0, 0)
        Call mouse_event(&H4, 0, 0, 0, 0)
        i = i * (-1)
    Wend
End Sub

Sub BlackCanvas()
Dim xTotal As Long, yTotal As Long
xTotal = 1572
yTotal = 1572



ThisWorkbook.Sheets("tela").Range("A1:BHL1572").Interior.Color = rgb(0, 0, 0)


End Sub

Sub PaintStar(x As Long, y As Long, s As Long, rgb As Long)
    For i = x - s To x + s
    If i > 0 And i < 1573 Then
        For j = y - s To y + s
        If j > 0 And j < 1573 Then
            ThisWorkbook.Sheets("tela").Cells(i, j).Interior.Color = rgb
        End If
        Next j
    End If
    Next i
End Sub

Sub IdentifyColors()
    Dim x As Long
    For i = 1 To 12
        x = ThisWorkbook.Sheets("teste").Range("B" & i).Interior.Color
        ThisWorkbook.Sheets("teste").Range("C" & i).Value = x
    Next i
End Sub

Sub Stars()
Dim deltaX As Integer, deltaY As Integer, nStars As Long, x As Long, y As Long, a As Long, b As Long, n As Long, c As Long
nStars = 1755
BlackCanvas
For s = nStars To 1 Step -1
    If ThisWorkbook.Sheets("estrelas").Range("AA" & (s + 1)).Value Then
        x = ThisWorkbook.Sheets("estrelas").Range("Y" & (s + 1)).Value + 1
        y = ThisWorkbook.Sheets("estrelas").Range("Z" & (s + 1)).Value + 1
        n = ThisWorkbook.Sheets("estrelas").Range("AB" & (s + 1)).Value + 1
        c = ThisWorkbook.Sheets("estrelas").Range("AC" & (s + 1)).Value + 1
        PaintStar 1573 - x, y, n, c
'        If ThisWorkbook.Sheets("estrelas").Range("I" & (s + 1)).Value = ThisWorkbook.Sheets("estrelas").Range("AF2").Value Then
'            PaintStar 1573 - x, y, n, 255
'        Else
'            PaintStar 1573 - x, y, n, 16777215
'        End If
    End If
Next s
End Sub
