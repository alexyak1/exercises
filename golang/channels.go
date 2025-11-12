package channels

import "fmt"

func writer() chan int {
	ch := make(chan int)
	go func() {
		for i := range 10 {
			ch <- i + 1
		}
		close(ch)
	}()
	return ch
}

func channels() {
	ch := writer()
	for {
		val, ok := <-ch
		if !ok {
			break
		}

		fmt.Println("Received:", val)
	}
}
