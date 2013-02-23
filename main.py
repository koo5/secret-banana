#!/usr/bin/python
#-*- coding: utf-8 -*-







import os, sys
import pygame
from pygame import gfxdraw






left_margin = 10
screen_height = 600







pygame.init()
pygame.display.set_caption("777")
pygame.key.set_repeat(300,30)
screen_surface = pygame.display.set_mode((1000,screen_height))








font = pygame.font.SysFont('monospace', 16)
f= font.render(" ",False,(0,0,0)).get_rect()
fonth = f.height
fontw = f.width
screenlines = screen_height / fonth
f=None
left_margin = 12







code = [["sin", "5"],["cos","12"]]
cursorx = 0
wordx = 0
wordy = 0
dictionary = ["thing", "is a kind of"]
#todo: synonyma
menu = []
menu_sel = 0







def settext(w):
	global code
	code[wordy][wordx] = w

def gettext():
	return code[wordy][wordx]

def snapwordx():
	global wordx
	wordx = min(len(code[wordy]), wordx)
	if len(code[wordy]) == wordx:
		code[wordy].insert(0, "")
		#http://mail.python.org/pipermail/tutor/2005-March/036803.html


def moveup():
	global wordy, code, wordx
	if wordy == 0:
		code = [] + code
	else:
		wordy-=1
	snapwordx()

def movedown():
	global wordy, code, wordx
	wordy+=1
	if wordy >= len(code):
		code.append([])
	snapwordx()		

def moveright():
	global cursorx
	if cursorx < len(code[wordy][wordx]):
		cursorx += 1
	else:
		wordright()
def wordright():
	global wordx, code, cursorx
	wordx += 1
	if wordx >= len(code[wordy]):
		code[wordy].append("")
	cursorx = 0

def moveleft():
	global cursorx
	if cursorx > 0:
		cursorx -= 1
	else:	
		wordleft()

def wordleft():
	global wordx, cursorx
	if wordx > 0:
		wordx -= 1
		cursorx = len(code[wordy][wordx])







def initiate_new_word():
	menu_sel = 0








def update_menu():

#	make a list of all dictionary words beginning with the edited word
	menu = [w for w in dictionary if word in w]
	print "todays menu:", menu










def draw():
	screen_surface.fill((0,0,0))

	y = 0
	wy = 0
	for l in code:
		x = 0
		wx = 0
		for w in l:
			if (wx == wordx) and (wy == wordy):
				to_blit=font.render(w,True,(255,255,255))
			else:
				to_blit=font.render(w,True,(122,255,122))
			screen_surface.blit(to_blit,(left_margin+x, y))
			x = x + to_blit.get_width() + 10
			wx += 1
		y += fonth
		wy += 1

	letters = 0
	for i in range(0, wordx):
		letters += len(code[wordy][i])+1
	letters += cursorx
	print "cursorx is ",cursorx,", drawing cursor at ",letters," letters"	

	startpos = (left_margin+(letters*fontw), wordy*fonth)
	endpos   = (left_margin+(letters*fontw), (wordy+1)*fonth)
	pygame.draw.aaline(screen_surface, (200, 200, 0), startpos, endpos,3)


	pygame.display.update()












def control(event):
	global menu_sel,cursorx,code, wordx


	# up & down
	if event.key == pygame.K_DOWN:
		movedown()
	if event.key == pygame.K_UP:
		moveup()

	# pg up & down
	if event.key == pygame.K_PAGEDOWN:
		menu_sel +=1
	if event.key == pygame.K_PAGEUP:
		menu_sel -=1

	# left & right
	if event.key == pygame.K_LEFT:
		moveleft()
	if event.key == pygame.K_RIGHT:
		moveright()




	if event.key == pygame.K_HOME:
		cursorx = 0
		wordx = 0
	if event.key == pygame.K_END:
		wordx = -1+len(code[wordy])
		cursorx = len(gettext())



	if event.key == pygame.K_F8:
	        del code[wordy]



	if event.scancode == 151 or event.key == pygame.K_F12:
	        #exit
#		save()
		bye()
	if event.key == pygame.K_F10:
 		bye()
	if event.scancode == 37:#run?
		pass






def edit(event):
	global cursorx
	if event.key==pygame.K_BACKSPACE:
		if cursorx > 0 and cursorx <= len(gettext()):
			settext(gettext()[0:cursorx-1]+gettext()[cursorx:])
			cursorx -=1
	elif event.key==pygame.K_DELETE:
		if cursorx >= 0 and cursorx < len(gettext()):
			settext(gettext()[0:cursorx]+gettext()[cursorx+1:])
	if event.unicode:
		settext(gettext()[0:cursorx]+event.unicode+gettext()[cursorx:])
		cursorx +=1






def process_event(event):
	if event.type == pygame.QUIT:
		bye()
	if event.type == pygame.KEYDOWN:
		control(event) or edit(event)





def loop():
	process_event(pygame.event.wait())
	draw()


while 1:
	try:
		loop()
	except KeyboardInterrupt() as e:
		pygame.display.iconify()
		raise e
	except Exception() as e:
		pass



