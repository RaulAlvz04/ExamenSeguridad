from collections import Counter

def realizarCambio(texto):
	print("\n")
	letra1=input("Introduce que letra quieres cambiar :)")
	letra2=input("Introduce la letra por la que la quieres cambiar :(")
	return texto.replace(letra1,letra2)
	
def main():
	texto="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
	
	letras=Counter(texto)
	print("Las tres más frecuentes son:")
	letras_frecuentes=letras.most_common(3)
	print(letras_frecuentes)
	print("\n")
	
	resultado=texto
	print("Sabemos que en castellano las letras más comunes son la 'e' y la 'a', asi que metemos ambas letras por las letras más comunes en nuestro texto")
	print("\n")
	
	resultado=resultado.replace(letras_frecuentes[1][0], 'e')
	resultado=resultado.replace(letras_frecuentes[2][0], 'a')
	
	print(resultado)
	print("\n")
	
	print("Ahora intenta descifrar las demas letras")
	print("\n")
	resultado=realizarCambio(resultado)
	
	seguir="s"
	while seguir=="s":
		print("\n")
		print(resultado)
		print("\n")
		seguir=input("¿Quieres hacer más cambios(s/n)").strip().lower()
		if seguir != "s":
			print("ADIOS")
			break
		resultado=realizarCambio(resultado)
		
		
main()
	
