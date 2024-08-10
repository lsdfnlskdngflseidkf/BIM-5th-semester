flower(lily).
flower(lotus).
flower(daisy).
flower(dahila).

fruit(mango).
fruit(papaya).
fruit(pomegranate).
fruit(watermelon).

likes(ram,mango).
likes(ram,lotus).
likes(sital,papaya).
likes(sital,watermelon).
likes(isita,X):-fruit(X).
likes(isita,X):-flower(X).
likes(ram,dahila).
