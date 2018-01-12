TypeScript 
	引子：null undefined
	类型注解：TS的基础类型
	
	:boolean
	:number
	:string--模板字符串
	
	数组 :number[]
	数组泛型 Array<元素类型>
	
	元组 Tuple :[string,number]已知元素数量和类型的数组，各元素的类型不必相同
	
	联合类型-----
	
	枚举 enum Color{Red,Green,Blue}
	:Color
	
	:any
	:void
	:null
	:undefined
	
	默认情况下null和undefined是所有类型的子类型。 就是说你可以把 null和undefined赋值给number类型的变量。
然而，当你指定了--strictNullChecks标记，null和undefined只能赋值给void和它们各自。 这能避免很多常见的问题。 也许在某处你想传入一个 string或null或undefined，你可以使用联合类型string | null | undefined。

	:never
	
	
	接口 
	可选属性
	interface SquareConfig{
		color?:string;
		width?number;
	}
	
	只读属性
	interface Point{
		readonly x:number;
		readonly y:number;
	}
	赋值后，则不能改变
	ReadonlyArray<T>类型，它与Array<T>相似，只是把所有可变方法去掉了，因此可以确保数组创建后再也不能被修改
	可以看到就算把整个ReadonlyArray赋值到一个普通数组也是不可以的。 但是你可以用类型断言重写：像极了C#的Clone
	如果一个对象字面量存在任何“目标类型”不包含的属性时，你会得到一个错误。
	
	绕开这些检查非常简单。 最简便的方法是使用类型断言：
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	