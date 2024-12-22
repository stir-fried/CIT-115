#planent surface gravity factors
nMERCURY_FACTOR = 0.38
nVENUS_FACTOR = 0.91
nMOON_FACTOR = 0.165
nMARS_FACTOR = 0.38
nJUPITER_FACTOR = 2.34
nSATURN_FACTOR = 0.93
nURANUS_FACTOR = 0.92
nNEPTUNE_FACTOR = 1.12
nPLUTO_FACTOR = 0.066

#ask for name
sUserName = input('What is your name? ')
#ask for{ Weight and convert to flt
nUserWeight = float(input('What is your weight? '))

print(f'What is your name: {sUserName}')
print(f'What is your weight: {nUserWeight}')

#prints user's name and calculated weights, user weight*planet factor

print(f"{sUserName} here are your weights on our Solar system's planets:")
print(f'{"Weight on Mercury:":25}{nUserWeight*nMERCURY_FACTOR:10.2f}')
print(f'{"Weight on Venus":25}{nUserWeight*nVENUS_FACTOR:10.2f}')
print(f'{"Weight on our Moon:":25}{nUserWeight*nMOON_FACTOR:10.2f}')
print(f'{"Weight on Mars:":25}{nUserWeight*nMARS_FACTOR:10.2f}')
print(f'{"Weight on Jupiter:":25}{nUserWeight*nJUPITER_FACTOR:10.2f}')
print(f'{"Weight on Saturn:":25}{nUserWeight*nSATURN_FACTOR:10.2f}')
print(f'{"Weight on Uranus:":25}{nUserWeight*nURANUS_FACTOR:10.2f}')
print(f'{"Weight on Neptune:":25}{nUserWeight*nNEPTUNE_FACTOR:10.2f}')
print(f'{"Weight on Pluto:":25}{nUserWeight*nPLUTO_FACTOR:10.2f}')