Evolver
=======

Evolving program like cleverbot

Hi, this is a simple python program that is meant to replicate a 'cleverbot' type program by responding to known user
input randomly and asking about input it does not understand. Once the unknown input has been defined the program stores
it in a dictionary so it can reference it next time that input is used. 

The 'evolve.py' file is the main file and references functions from the 'extras.py' file

Furthermore to actually use this program you will need the 3 other files I have titled "defs.txt", 
"responses.txt", and "users.txt".
 
 If you would like to test how the program works, try asking it "do you like [insert a noun]" If the noun is not in the dictionary, the response will be "what is a [noun]". You may then define it and ask "what is a [noun]" and the response will be the deffinition you just provided.
 
 *Finally this program was written with python 3.0.1 so ensure you have the latest version for it to work properly* 
 
Evolver is free under the MIT license

The MIT License (MIT)

Copyright (c) [2014] [Connor Herring]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
