from django.shortcuts import render, redirect
import random

def ninjaGold(request):
    if 'current_gold' not in request.session:
        request.session['current_gold'] = 0
        request.session['activities'] = []

# SET SOME WIN CONDITIONS

    context = {
        'activity' : reversed(request.session['activities'])
    }
    return render(request, 'ng_temp.html', context)

#to refactor this I might set a dictionary.
#Keys will match the locations and I can pass values to "randint()".
#Then lose all the conditionals to have a "single" processor.
def processor(request):

    if request.method == "POST":
        if request.POST['location'] == 'farm':
            amount = random.randint(10,40)
            request.session['current_gold'] += amount
            print(f"$$$$$$$$$$$$$$$$$ {amount} gold from the farm! $$$$$$$$$$$$$$$$$")
            farmLog = f"Earned {amount} gold from the farm!"
            log = request.session['activities']
            log.append(farmLog)
            
        if request.POST['location'] == 'house':
            amount = random.randint(5,20)
            request.session['current_gold'] += amount
            print(f"$$$$$$$$$$$$$$$$$ {amount} gold from the house! $$$$$$$$$$$$$$$$$")
            houseLog = f"Earned {amount} gold from the house!"
            log = request.session['activities']
            log.append(houseLog)
            
            #future feature for cave- weighted generation to get lower amounts more
        if request.POST['location'] == 'cave':
            amount = random.randint(1,100)
            request.session['current_gold'] += amount
            print(f"$$$$$$$$$$$$$$$$$ {amount} gold from the cave! $$$$$$$$$$$$$$$$$")
            caveLog = f"Found {amount} gold in a cave!"
            log = request.session['activities']
            log.append(caveLog)
                    
        if request.POST['location'] == 'casino':
            amount = random.randint(-100,100)
            request.session['current_gold'] += amount
            print(f"$$$$$$$$$$$$$$$$$ {amount} gold from the casino! $$$$$$$$$$$$$$$$$")
            log = request.session['activities']
            if amount > 0:
                casinoLog = f"Won {amount} gold from the casino!"
                log.append(casinoLog)
            elif amount < 0:
                casinoLog = f"Lost {amount} gold from the casino!"
                log.append(casinoLog)


    return redirect('/')

def destroyer(request):#reset the game
    request.session.clear()
    return redirect('/')
