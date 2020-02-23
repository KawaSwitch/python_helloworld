#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, pygame.locals
import time

def main():
	pygame.init()

	# joystick detection
	try:
		pygame.joystick.init()
		joystick = pygame.joystick.Joystick(0)
		joystick.init()
		print('joystick found: ' + joystick.get_name())
	except pygame.error:
		print('joystick not found')
		return

	# event loop
	while True:
		for e in pygame.event.get():
			if e.type == pygame.locals.QUIT: # Ctrl+C
				return

			if e.type == pygame.locals.JOYAXISMOTION:
				x, y = joystick.get_axis(0), joystick.get_axis(1)
				print('axis x:' + str(x) + ' axis y:' + str(y))
			elif e.type == pygame.locals.JOYHATMOTION:
				x, y = joystick.get_hat(0)
				print('hat x:' + str(x) + ' hat y:' + str(y))
			elif e.type == pygame.locals.JOYBUTTONDOWN:
				print('button:' + str(e.button))
		
if __name__ == '__main__':
	try:
		main()
	except pygame.error:
		print('joystick not found')