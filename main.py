import tweepy
import schedule
import time
import random

consumer_key = 'cehmZzgLzPWlSwPiWgXnVy5wG'
consumer_secret = 'XwXJkpijV13IKYgu1oyym80oNhKtfHuwnCpN60SvNtGiZ562gt'

key = '1382386059934318594-cgSBNjEjz450k4aU5X2XWQwnmUDS3E'
secret = 'Cgt5Sugrlf5CCDh9DoEjMQyWpmbt2mTmh2fTmPfa60KmL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

a_array = ['Alonso>>>>Vettel', 'Obviamente el nano es el mejor', 'Que yo sepa, Vettel no ha ganado nunca saliendo desde fuera del Top 3', '🅱️ettel tetrafraude', '22 de julio de 2018', 'El nano tenia un coche mierda y casi gana el mundial y Vettel? un auto dominante', 'Alonso tiene 1 calle en Oviedo, cuantas tiene 🅱️ettel?', '¿Que cuántos mundiales tiene 🅱️ettel y cuantos El Nano? \nlos mismos que Vettel consiguió con Ferrari, 2 mas teniendo un coche que no es el mejor de la parrilla y a saber cuantos con ese redbull y adrian newey']
insultos = ['tonto, Tonto, tonto., Tonto.']
saludo = ['hola', 'holaa', 'Hola']

def read_last_id():
	file = open('last_id.txt', 'r')
	id = int(file.read().strip())
	file.close()
	return id

def store_last_id(id):
	file = open('last_id.txt', 'w')
	file.write(str(id))
	file.close()

def reply_a(tweet):
	api.update_status(
		'@' + tweet.user.screen_name + ' ' + random.choice(a_array),
		tweet.id
	)
	store_last_id(tweet.id)

def reply_and_block(tweet):
	api.update_status(
		'@' + tweet.user.screen_name + ' ' + 'pos a tu madre me la monto, te falta foro😎🥵',
		tweet.id
	)
	store_last_id(tweet.id)

def reply_hola(tweet):
	api.update_status(
		'@' + tweet.user.screen_name + ' ' + 'tu nariz contra mis bolas, te falta foro😎🥵',
		tweet.id
	)
	store_last_id(tweet.id)


def tweet_a():
	api.update_status(random.choice(a_array))

def tweet_PedroMDLR():
	api.update_status('Magic Pedro de la Rosa, vuelta rápida en Bahrein 1:31:447 #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR #PedroMDLR ')

def check_mentions():
	mentions = api.mentions_timeline(read_last_id(), tweet_mode = 'extended')
	for tweet in reversed(mentions):
		print(tweet.full_text)
		if any(x in tweet.full_text for x in insultos):
			reply_and_block(tweet)
		elif any(x in tweet.full_text for x in saludo):
			reply_hola(tweet)
		else:
			reply_a(tweet)


def main():
	schedule.every(7).seconds.do(check_mentions)
	schedule.every().day.at('10:00').do(tweet_a)
	schedule.every().day.at('18:00').do(tweet_a)
	schedule.every().day.at('15:00').do(tweet_PedroMDLR)
	

	while True:
		try:
			schedule.run_pending()
			time.sleep(2)
		except tweepy.TweepError as e:
			raise e

if __name__ == "__main__":
	main()