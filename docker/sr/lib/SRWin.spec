# 0 /home/ubuntu/sr/library/gsrwin.sr 3+

global SRWin


 const DefaultPoll := 100
 const UseDefault := 0
 const OffScreen := 1

 type winVoid = ptr any
 type winWindow = winVoid
 type winFont = winVoid
 type winImage = winVoid

 type winInitialState = int
 type winError = int

 type winPoint = rec ( x , y : int )
 type winRectangle = rec ( x , y , w , h : int )






 type winEventType = int
 const Ev_None := 0
 const Ev_ButtonDown := 1
 const Ev_ButtonUp := 2
 const Ev_KeyDown := 4
 const Ev_KeyUp := 8
 const Ev_PointerMove := 16
 const Ev_EnterWindow := 32
 const Ev_ExitWindow := 64
 const Ev_DeleteWindow := 128
 const Ev_All := Ev_ButtonDown |
 Ev_ButtonUp |
 Ev_KeyDown |
 Ev_KeyUp |
 Ev_PointerMove |
 Ev_EnterWindow |
 Ev_ExitWindow |
 Ev_DeleteWindow

 type winButtonKeyStatus = int
 const BK_None := 0
 const BK_Button1 := 1
 const BK_Button2 := 2
 const BK_Button3 := 4
 const BK_Button4 := 8
 const BK_Button5 := 16
 const BK_SHIFT := 32
 const BK_LOCK := 64
 const BK_CNTRL := 128
 const BK_Mod1 := 256
 const BK_Mod2 := 512
 const BK_Mod3 := 1024
 const BK_Mod4 := 2048
 const BK_Mod5 := 4096

 type winLineStyle = enum ( LineSolid ,
 LineDoubleDash ,
 LineOnOffDash )

 type winCapStyle = enum ( CapNotLast ,
 CapButt ,
 CapRound ,
 CapProjecting )

 type winJoinStyle = enum ( JoinMiter ,
 JoinRound ,
 JoinBevel )

 type winFillStyle = enum ( FillSolid ,
 FillTiled ,
 FillOpaqueStippled ,
 FillStippled )

 type winFillRule = enum ( FillEvenOddRule ,
 FillWindingRule )

 type winArcMode = enum ( ArcChord ,
 ArcPieSlice )

 type winStdCursor = enum (
 XC_X_cursor , XC_arrow ,
 XC_based_arrow_down , XC_based_arrow_up ,
 XC_boat , XC_bogosity ,
 XC_bottom_left_corner , XC_bottom_right_corner ,
 XC_bottom_side , XC_bottom_tee ,
 XC_box_spiral , XC_center_ptr ,
 XC_circle , XC_clock ,
 XC_coffee_mug , XC_cross ,
 XC_cross_reverse , XC_crosshair ,
 XC_diamond_cross , XC_dot ,
 XC_dotbox , XC_double_arrow ,
 XC_draft_large , XC_draft_small ,
 XC_draped_box , XC_exchange ,
 XC_fleur , XC_gobbler ,
 XC_gumby , XC_hand1 ,
 XC_hand2 , XC_heart ,
 XC_icon , XC_iron_cross ,
 XC_left_ptr , XC_left_side ,
 XC_left_tee , XC_leftbutton ,
 XC_ll_angle , XC_lr_angle ,
 XC_man , XC_middlebutton ,
 XC_mouse , XC_pencil ,
 XC_pirate , XC_plus ,
 XC_question_arrow , XC_right_ptr ,
 XC_right_side , XC_right_tee ,
 XC_rightbutton , XC_rtl_logo ,
 XC_sailboat , XC_sb_down_arrow ,
 XC_sb_h_double_arrow , XC_sb_left_arrow ,
 XC_sb_right_arrow , XC_sb_up_arrow ,
 XC_sb_v_double_arrow , XC_shuttle ,
 XC_sizing , XC_spider ,
 XC_spraycan , XC_star ,
 XC_target , XC_tcross ,
 XC_top_left_arrow , XC_top_left_corner ,
 XC_top_right_corner , XC_top_side ,
 XC_top_tee , XC_trek ,
 XC_ul_angle , XC_umbrella ,
 XC_ur_angle , XC_watch ,
 XC_xterm , XC_None )

 type winCursor = winVoid

 type winColor = string [ * ]
 type winPixel = winVoid


 type winDrawOp = enum ( Op_Clear ,
 Op_And ,
 Op_AndReverse ,
 Op_Copy ,
 Op_AndInverted ,
 Op_Noop ,
 Op_Xor ,
 Op_Or ,
 Op_Nor ,
 Op_Equiv ,
 Op_Invert ,
 Op_OrReverse ,
 Op_CopyInverted ,
 Op_OrInverted ,
 Op_Nand ,
 Op_Set )

 type winEvent = rec ( event_type : winEventType ;
 window : winWindow ;
 x , y : int ;
 bk_status : int ;
 data : int ;
 keysym : int
 )

 optype winEventChannel ( winEvent ) { send }





 op WinOpen ( display : string [ * ] ;
 title : string [ * ] ;
 evchannel : cap winEventChannel ;
 state : winInitialState ;
 w , h : int ) returns win : winWindow

 op WinClose ( win : winWindow )

 op WinCreateSubwindow ( oldwin : winWindow ; evchannel : cap
 winEventChannel ; state : winInitialState ; x , y , w , h : int )
 returns newwin : winWindow

 op WinDestroyWindow ( win : winWindow )

 op WinSetBorder ( win : winWindow ; width : int ; color : winColor )
 returns pv : winPixel

 op WinNewContext ( oldwin : winWindow ) returns newwin : winWindow
 op WinCopyContext ( srcwin , destwin : winWindow )

 op WinFlush ( win : winWindow )
 op WinSync ( win : winWindow ; discard : bool )

 op WinBell ( win : winWindow ; percent : int )

 op WinDrawPixel ( win : winWindow ; pt : winPoint )

 op WinDrawLine ( win : winWindow ; pt1 , pt2 : winPoint )
 op WinDrawPolyline ( win : winWindow ; pts [ * ] : winPoint )
 op WinDrawPolygon ( win : winWindow ; pts [ * ] : winPoint )
 op WinFillPolygon ( win : winWindow ; pts [ * ] : winPoint )

 op WinDrawRectangle ( win : winWindow ; rect : winRectangle )
 op WinFillRectangle ( win : winWindow ; rect : winRectangle )

 op WinDrawArc ( win : winWindow ; box : winRectangle ; a1 , a2 : int )
 op WinFillArc ( win : winWindow ; box : winRectangle ; a1 , a2 : int )

 op WinClearArea ( win : winWindow ; area : winRectangle )
 op WinEraseArea ( win : winWindow ; area : winRectangle )
 op WinCopyArea ( srcw , destw : winWindow ; src_rect : winRectangle ;
 destp : winPoint )

 op WinSetLabels ( win : winWindow ; wlab , ilab : string [ * ] )

 op WinSetPoll ( win : winWindow ; ticks : int )
 op WinSetEventMask ( win : winWindow ; em : int )

 op WinMapWindow ( win : winWindow )
 op WinUnmapWindow ( win : winWindow )
 op WinMapSubwindows ( win : winWindow )
 op WinUnmapSubwindows ( win : winWindow )
 op WinRaiseWindow ( win : winWindow )
 op WinLowerWindow ( win : winWindow )
 op WinMoveWindow ( win : winWindow ; pt : winPoint )
 op WinEnableOutput ( win : winWindow )
 op WinDisableOutput ( win : winWindow )
 op WinUpdateWindow ( win : winWindow )

 op WinSetForeground ( win : winWindow ; fg : winColor ) returns pv : winPixel
 op WinSetBackground ( win : winWindow ; bg : winColor ) returns pv : winPixel
 op WinSetForegroundByPixel ( win : winWindow ; pv : winPixel )
 op WinSetBackgroundByPixel ( win : winWindow ; pv : winPixel )

 op WinSetClipRectangles ( win : winWindow ; origin : winPoint ; rects [ * ] :
 winRectangle )

 op WinSetLineAttr ( win : winWindow ; line_width : int ; line_style :
 winLineStyle ; cap_style : winCapStyle ; join_style : winJoinStyle )
 op WinSetFillAttr ( win : winWindow ; fill_style : winFillStyle ;
 fill_rule : winFillRule )
 op WinSetDashes ( win : winWindow ; dash_offset : int ; dash_list : string [ * ] )
 op WinSetArcMode ( win : winWindow ; arc_mode : winArcMode )
 op WinSetDrawOp ( win : winWindow ; dop : winDrawOp )

 op WinDefaultFont ( win : winWindow ) returns font : winFont
 op WinLoadFont ( win : winWindow ; fontname : string [ * ] ) returns font : winFont
 op WinSetFont ( win : winWindow ; font : winFont )
 op WinFreeFont ( win : winWindow ; font : winFont )

 op WinTextWidth ( font : winFont ; str : string [ * ] ) returns width : int
 external WinFontAscent ( winFont ) returns int
 external WinFontDescent ( winFont ) returns int

 op WinDrawString ( win : winWindow ; pt : winPoint ; str : string [ * ] )
 op WinDrawImageString ( win : winWindow ; pt : winPoint ; str : string [ * ] )

 op WinCreateCursor ( win : winWindow ; stdcursor : winStdCursor )
 returns cur : winCursor
 op WinSetCursor ( win : winWindow ; cursor : winCursor ; fg , bg :
 winColor ) returns err : winError
 op WinFreeCursor ( win : winWindow ; cursor : winCursor )

 op WinCreateImage ( win : winWindow ; depth , w , h : int ) returns im : winImage
 op WinGetPixel ( im : winImage ; pt : winPoint ) returns pv : winPixel
 op WinPutPixel ( im : winImage ; pt : winPoint ; pv : winPixel )
 op WinAddPixel ( im : winImage ; pv : winPixel )
 op WinPutImage ( win : winWindow ; im : winImage ; src_rect : winRectangle ;
 dest : winPoint )
 op WinGetImage ( win : winWindow ; im : winImage ; src_rect : winRectangle ;
 dest : winPoint )
 op WinDestroyImage ( im : winImage )


 body SRWin ; end ;
