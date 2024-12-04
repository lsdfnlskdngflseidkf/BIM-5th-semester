flower(lily).
flower(lotus).
flower(daisy).
flower(Dahila).

fruit(mango).
fruit(papaya).
fruit(pomegranate).
fruit(watermelon).

likes(ram,mango).
likes(ram,Lotus).
likes(sital,papaya).
likes(sital,watermelon).
likes(ram,dahila).
likes(isita,X):-fruit(X).
likes(isita,X):-flower(X).
