import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = "=", case_insenstive  = True)

class C(object):
    def init(self):
        self._x = None
        self._y = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @y.deleter
    def y(self):
        del self._y

c = C()

@client.event
async def on_ready():
  print('Estamos on!')

@client.command()
async def ola(ctx):
  await ctx.send(f'opa meu consagrado')

@client.command()
async def quem_e(ctx):
  await ctx.send(f'sou eu, é o probs, dale')

@client.command()
async def comandos(ctx):
  await ctx.send(f'(ola; quem_e; desafio "numero"; minimo (valor); maximo (valor))')

@client.command()
async def desafio(ctx, numero):
  numero_certo = int(numero)
  valor = random.randint(int(c.x), int(c.y))
  if valor == numero_certo:
        await ctx.send("voce acertou, lindo!")
  else:
        await ctx.send(f'voce errou, tanso. numero era {valor}')

@client.command()
async def minimo(ctx, numero):
  c.x = numero
  await ctx.send(f'setado como {numero}.')

@client.command()
async def maximo(ctx, numero):
  c.y = numero
  await ctx.send(f'setado como {numero}.')


client.run('é o probs')
