package main

import (
	"strconv"
	"syscall/js"
)

func getElementById(id string) js.Value {
	return js.Global().Get("document").Call("getElementById", id)
}

func inc(this js.Value, args []js.Value) interface{} {
	var element = getElementById("int")
	currentValue, err := strconv.Atoi(element.Get("innerHTML").String())
	if err != nil {
		currentValue = 0
	}
	element.Set("innerHTML", strconv.Itoa(currentValue+1))
	return nil
}

func dec(this js.Value, args []js.Value) interface{} {
	var element = getElementById("int")
	currentValue, err := strconv.Atoi(element.Get("innerHTML").String())
	if err != nil {
		currentValue = 0
	}
	element.Set("innerHTML", strconv.Itoa(currentValue-1))
	return nil
}

func res(this js.Value, args []js.Value) interface{} {
	var element = getElementById("int")
	element.Set("innerHTML", "0")
	return nil
}

func main() {
	c := make(chan struct{}, 0)
	js.Global().Set("inc", js.FuncOf(inc))
	js.Global().Set("dec", js.FuncOf(dec))
	js.Global().Set("res", js.FuncOf(res))
	<-c
}
