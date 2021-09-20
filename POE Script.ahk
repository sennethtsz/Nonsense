#IfWinActive, ahk_class POEWindowClass

`::
{
	;Initialize random delays between 30 and 80 ms (arbitrary values, may be changed)
	random, delay2, 30, 80
	random, delay3, 30, 80
	random, delay4, 30, 80
	random, delay5, 30, 80
	random, delay6, 30, 80

	send, 1

	sleep, %delay2%
	send, 2

	sleep, %delay3%
	send, 3

	sleep, %delay4%
	send, 4

	sleep, %delay5%
	send, 5

	;sleep, %delay6%
	;send, 0 

}
return

;--------------------------------------------------------------------------------------------------------------
#MaxThreadsPerHotkey 3

F7::
Toggle := !Toggle
Loop
{
If (!Toggle)
Break
Click
Sleep 83 ; Make this number higher for slower clicks, lower for faster.
}
Return

;--------------------------------------------------------------------------------------------------------------
#MaxThreadsPerHotkey 3

F6::
mode := !mode ; Set mode either to 1 or 0 - toggle
return

#If WinActive("ahk_class POEWindowClass") && mode = 1
$LButton::
Send, {LButton}
Keywait, LButton, T0.2
If ErrorLevel {
Send, {LButton down}{t down}
Keywait, LButton
Send, {LButton up}{t up}
}
Return