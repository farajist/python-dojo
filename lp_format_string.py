template = '{0}, {1} and {2}'
print(template.format('spam', 'ham', 'eggs'))
# 'spam, ham and eggs'
template = '{motto}, {beef} and {food}'
print(template.format(motto='spam', beef='ham', food='eggs'))
# 'spam, ham and eggs'
template = '%s, %s and %s'
print(template % ('spam', 'ham', 'eggs'))
# 'spam, ham and eggs'
template = '%(motto)s, %(beef)s and %(food)s'
print(template % dict(motto='spam', beef='ham', food='eggs'))
# 'spam, ham and eggs'
somelist = list('SPAM')
print(somelist)

print('first={0[0]}, third={0[2]}'.format(somelist))
# 'first=S, third=A'
print('first={0}, last={1}'.format(somelist[0], somelist[-1]))
# 'first=S, last=M'
print(somelist[-1])
# 'M'
print('%s' % (somelist[-1]))
# 'M'
parts = somelist[0], somelist[-1], somelist[1:3]
print(parts)
# ('S', 'M', ['P', 'A'])
print('first={0}, last={1}. middle={2}'.format(*parts))
# "first=S, last=M. middle=['P', 'A']"

print('{0:10} = {1:10}'.format('spam', 123.4567))
# 'spam       =   123.4567'
import sys
print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))
# '     linux = laptop    '
print('{0.platform:>10} = {1[kind]:^10}'.format(sys, dict(kind='laptop')))
# '     linux =   laptop  '
print(1/3.0)
# 0.3333333333333333
print('{0:.{1}f}'.format(1/3.0, 4))
# '0.3333'
print('{0:.{1}f}'.format(1/3.0, 10))
# '0.3333333333'
print(format(1.2345, '.2f'))
# '1.23'
