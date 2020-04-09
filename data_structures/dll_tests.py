from double_linked_list import *

def test_push():
    colors = DoubleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors.push("Something Else Blue")
    assert colors.count() == 3

test_push()  

def test_pop():
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.count() == 2
    assert colors.pop() == "Alizarin"
    assert colors.count() == 1
    assert colors.pop() == "Magenta"
    assert colors.count() == 0
    assert colors.pop() == None

test_pop()

def test_unshift():
    colors = DoubleLinkedList()
    colors.push("Viridian")
    colors.push("Sap Green")
    colors.push("Van Dyke")
    assert colors.unshift() == "Viridian"
    assert colors.count() == 2
    assert colors.unshift() == "Sap Green"
    assert colors.count() == 1
    assert colors.unshift() == "Van Dyke"
    assert colors.count() == 0
    assert colors.unshift() == None
    assert colors.count() == 0
    
test_unshift()

def test_remove():
    colors = DoubleLinkedList()
    colors.push("Cobalt")
    colors.push("Zinc White")
    colors.push("Nickle Yellow")
    colors.push("Perinone")
    assert colors.remove("Cobalt") == 0
    assert colors.count() == 3
    assert colors.remove("Perinone") == 2
    assert colors.count() == 2
    assert colors.remove("Nickle Yellow") == 1
    assert colors.count() == 1
    assert colors.remove("Zinc White") == 0
    assert colors.count() == 0 

test_remove()

def test_first():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pthalo Green")
    assert colors.first() == "Pthalo Green"

test_first()

def test_last():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    assert colors.last() == "Hansa Yellow"

test_last()

def test_get():
    colors = DoubleLinkedList()
    colors.push("Vermillion")
    assert colors.get(0) == "Vermillion"
    colors.push("Sap Green")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "Vermillion"
    colors.pop()
    assert colors.get(0) == None

test_get()
