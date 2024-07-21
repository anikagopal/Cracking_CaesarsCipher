{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #This program is the starter code for the Cracking Caesar's Cipher Project. \
# This code is inspired by Cracking Codes with Python: An Introduction to Building and Breaking Ciphers by Al Sweigart https://www.nostarch.com/crackingcodes (BSD Licensed)\
\
import string\
\
# Global variables\
initialPosition = 0\
shiftedPosition = 0\
lettersLower = string.ascii_lowercase\
lettersUpper = string.ascii_uppercase\
numbers = string.digits\
symbols = string.punctuation\
possibleCharacters = lettersLower + lettersUpper + numbers + symbols\
\
\
# Define the function called decrypt\
def decrypt():\
  global shiftedPosition\
  shiftedPosition = initialPosition - key\
\
# Define the function called wraparound\
def wraparound():\
  global shiftedPosition\
  if shiftedPosition < 0:\
    shiftedPosition = shiftedPosition + len(possibleCharacters)\
\
# Run code\
\
# Introduction\
print("Welcome! This program will crack the Caesar cipher and figure out any secret message that was encrypted with the Caesar cipher. Type in your encrypted message and this program will print all of the key possibilities of your message below. \\n\\nYour message can only include the following characters: " + possibleCharacters + "\\n\\n")\
\
# Receive user input\
initialMessage = input("What is your encrypted message? ")\
input("\\nPress enter to generate all of the key possibilities for your encrypted message.\\n")\
\
# Cycle through all possible keys\
for key in range(len(possibleCharacters)):\
  shiftedMessage = ""\
  # Decrypt the message\
  for character in initialMessage:\
    if character in possibleCharacters:\
      initialPosition = possibleCharacters.find(character)\
      decrypt()\
      wraparound()\
  \
      shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]\
  \
    else: \
      shiftedMessage = shiftedMessage + character\
  \
  # Print the shifted message\
  print("Key #%s: %s" % (key, shiftedMessage))\
\
# Closing message\
print("\\nNow scroll through all of the key possibilities above and find the readable plaintext message.")}