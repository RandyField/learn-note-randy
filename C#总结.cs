// *******************************************************我是分割线 匿名类********************************************************************************************
/* #匿名类 
var annoyCla=new {
    ID=10010,
    Name="Randy",
    Age=25
} 

Reflector反编译
　　（1）匿名类被编译后会生成一个[泛型类]，可以看到上图中的<>f__AnonymousType0<<ID>j__TPar, <Name>j__TPar, <Age>j__TPar>就是一个泛型类；

　　（2）匿名类所生成的属性都是只读的，可以看出与其对应的字段也是只读的；

    （3）可以看出，匿名类还重写了基类的三个方法：Equals,GetHashCode和ToString；我们可以看看它为我们所生成的ToString方法是怎么来实现的：
*/

// *******************************************************我是分割线 泛型*****************************************************************************************************

    它有助于您最大限度地重用代码、保护类型的安全以及提高性能。
    
    您可以创建泛型集合类。.NET 框架类库在 System.Collections.Generic 命名空间中包含了一些新的泛型集合类。您可以使用这些泛型集合类来替代 System.Collections 中的集合类。
    
    您可以创建自己的泛型接口、泛型类、泛型方法、泛型事件和泛型委托。
    
    您可以对泛型类进行约束以访问特定数据类型的方法。
    
    关于【泛型数据类型中】【使用的类型的信息】可在【运行时】通过【使用反射】获取。

    //泛型(Generic)方法
    static void Swap<T>(ref T lhs,ref T rhs)
    {
        T temp;
        temp=lhs;
        lhs=rhs;
        rhs=temp;
    }

    //泛型委托
    delegate T NumberChanger<T>(T n);

    //在声明泛型方法/泛型类的时候，可以给泛型加上一定的约束来满足特定的一些条件
    public class CacheHelper<T> where T:new()
    {
        
    }

    T：结构（类型参数必须是值类型。可以指定除 Nullable 以外的任何值类型）
    T：类 （类型参数必须是引用类型，包括任何类、接口、委托或数组类型）
    T：new() （类型参数必须具有无参数的公共构造函数。当与其他约束一起使用时new() 约束必须最后指定）
    T：< 基类名> 类型参数必须是指定的基类或派生自指定的基类
    T：< 接口名称> 类型参数必须是指定的接口或实现指定的接口。可以指定多个接口约束。约束接口也可以是泛型的。
    T：U 

    在封装公共组件的时候，很多时候我们的类/方法不需要关注调用者传递的实体是"什么"，这个时候就可以使用泛型。

    比如：

    using System;
    using System.Web.Caching;

    namespace Xy.CacheManager
    {
    public class CacheHelper<T>
    {
        //获取缓存实体
        public static T Get(Cache cache,string cacheKey)
        {
            //....缓存操作
        } 
        //插入缓存
        public static void Set(Cache cache T tEntity,string cacheKey)
        {
            //....缓存操作
        }
    }
    }
// *******************************************************我是分割线 匿名方法*****************************************************************************************************

匿名方法（Anonymous methods） 提供了一种传递代码块作为委托参数的技术。匿名方法是没有名称只有主体的方法。

delegate void NumberChanger(int n);
...
NumberChanger nc = delegate(int x)
{
    Console.WriteLine("Anonymous Method: {0}", x);
};

//调用
nc();


// *******************************************************我是分割线 委托 泛型委托*****************************************************************************************************


//定义委托-买书
private delegate void BuyBook();

//定义方法-书店卖书
public static void Book()
{
    Console.WriteLine("我提供书籍");
}

//实例化委托       建立关系
BuyBook buybook=new BuyBook(Book);

//拿书
buybook();

//买一本书籍，每次都让我定义下，烦死了，有没有一种方法不去定义委托呢
Action BookAction=new Action(Book);
        BookAction();

//想买本其他书，那怎么办，我是不是要重新再次定义委托。
//其实不需要你只需要把参数穿过来就可以了。下面我们看Action<T>的用法
public static void Book(string Bookname)
{
    Console.WriteLine("我要买书，书名是:{0}",Bookname);
}

public static void Main(string[] args)
{
    Action<string> BookAction =new Action<string>(Book);
    BookAction("百年孤独");
}

// 我不仅要自己选择书籍，我还要在一个牛逼的书籍厂家买，
//有没有这种方式呢，那么告诉你有，Action<in T1,in T2>
static void Main(string[] args)
{
    Action<string,string> BookAction = new Action<string,string>(Book);
    BookAction("百年孤独","北京大书店");
}

public static void Book(string BookName,string ChangJia)
{
    Console.WriteLine("我是买书的是:{0}来自{1}",BookName,ChangJia);
}

// Func 解释 
//封装一个不一定具有参数（也许没有）
//但却返回 TResult 参数指定的类型值的 【方法】。

    //无参
    static void Main(string[] args)
    {
        Func<string> RetBook = new Func<string>(FuncBook);
        Console.WriteLine(RetBook);
    }

    public static string FuncBook()
    {
        return "送书来了";
    }

    //有参
    static void Main(string[] args)
    {
        Func<string,string> RetBook = new Func<string,string>(FuncBook);
        Console.WriteLine(RetBook("aaa"));
    }
    public static string FuncBook(string BookName)
    {
        return BookName;
    }

// 1：Action用于没有返回值的方法（参数可以根据自己情况进行传递）

// 2：Func恰恰相反用于有返回值的方法（同样参数根据自己情况情况）

// 3：记住无返回就用action，有返回就用Func

扩展：　   (1). delegate

          delegate我们常用到的一种声明

        　(2). Action

          Action是无返回值的泛型委托。

　　      Action 表示无参，无返回值的委托

　　      Action<int,string> 表示有传入参数int,string无返回值的委托

 　　     Action<int,string,bool> 表示有传入参数int,string,bool无返回值的委托

          Action<int,int,int,int> 表示有传入4个int型参数，无返回值的委托

　　      Action至少0个参数，至多16个参数，无返回值。

         (3). Func

　　      Func是有返回值的泛型委托

　　      Func<int> 表示无参，返回值为int的委托

　　      Func<object,string,int> 表示传入参数为object, string 返回值为int的委托

　　      Func<object,string,int> 表示传入参数为object, string 返回值为int的委托

　　      Func<T1,T2,,T3,int> 表示传入参数为T1,T2,,T3(泛型)返回值为int的委托

　　      Func至少0个参数，至多16个参数，根据返回值泛型返回。必须有返回值，不可void

        (4) .predicate

　　      predicate 是返回bool型的泛型委托

　　      predicate<int> 表示传入参数为int 返回bool的委托

　　      Predicate有且只有一个参数，返回值固定为bool

　　      例：public delegate bool Predicate<T> (T obj)

// *******************************************************我是分割线 事件的***********************************************************************************************************

//定义委托
public delegate void BoilerLogHandler(string status);

// 基于上面的委托定义事件
public event BoilerLogHandler BoilerEventLog;

// 该事件在生成的时候会调用委托。


BoilerEventLog+=new BoilerLogHandler(Logger);

 static void Logger(string info)
{
    Console.WriteLine(info);
}//end 

// *******************************************************我是分割线 特性 待补充***********************************************************************************************************
特性（Attribute）是用于在【运行时】传递程序中各种元素（比如类、方法、结构、枚举、组件等）的行为信息的声明性标签。

可以通过使用特性向程序添加【声明性信息】。一个声明性标签是通过放置在它所应用的元素前面的方括号（[ ]）来描述的。


// *******************************************************我是分割线 C#中 Thread，Task，Async/Await，IAsyncResult 的那些事儿！***********************************************************************************************************

//1.线程
//IsBackground=true,将其设置为后台线程
Thread t = nwe Thread(Run){IsBackground=true};

//线程启动
t.Start();

Thread.Sleep(150000);

//主线程结束，后台线程会自动结束，不管有没有执行完成


//定义方法
static void Run()
{

}
//2.线程池
试想一下，如果有大量的任务需要处理，

例如网站后台对于HTTP请求的处理，

那是不是要对每一个请求创建一个后台线程呢？

显然不合适，这会占用大量内存，而且频繁地创建的过程也会严重影响速度，

那怎么办呢？

线程池就是为了解决这一问题，把创建的线程存起来，

形成一个线程池(里面有多个线程)，

当要处理任务时，

若线程池中有空闲线程(前一个任务执行完成后，线程不会被回收，会被设置为空闲状态)，

则直接调用线程池中的线程执行(例asp.net处理机制中的Application对象)，

for (int i = 0; i < length; i++)
{
    ThreadPool.QueueUserWorkItem(m=>{
    Console.WriteLine(Thread.CurrentThread.ManageThreadId.ToString());
    })
}

Console.Read();

//4、Semaphore负责协调线程，可以限制对某一资源访问的线程数量
static SemaphoreSlim semLim = new SemaphoreSlim(3); //3表示最多只能有三个线程同时访问
static void Main(string[] args)
{
    for (int i = 0; i < 10; i++)
    {
        new Thread(SemaphoreTest).Start();
    }
    Console.Read();
}
static void SemaphoreTest()
{
    semLim.Wait();
    Console.WriteLine("线程" + Thread.CurrentThread.ManagedThreadId.ToString() + "开始执行");
    Thread.Sleep(2000);
    Console.WriteLine("线程" + Thread.CurrentThread.ManagedThreadId.ToString() + "执行完毕");
    semLim.Release();
}

// 可以看到，刚开始只有三个线程在执行，当一个线程执行完毕并释放之后，才会有新的线程来执行方法！

// 除了SemaphoreSlim类，还可以使用Semaphore类，感觉更加灵活，


//5、Task
Task是.NET4.0加入的，跟线程池ThreadPool的功能类似，
用Task开启新任务时，会从线程池中调用线程，
而Thread每次实例化都会创建一个新的线程

Console.WriteLine("主线程启动");
//Task.Run启动一个线程
//Task启动的是后台线程，要在主线程中等待后台线程执行完毕，可以调用Wait方法
//Task task = Task.Factory.StartNew(() => { Thread.Sleep(1500); Console.WriteLine("task启动"); });
Task task = Task.Run(() => { 
    Thread.Sleep(1500);
    Console.WriteLine("task启动");
});
Thread.Sleep(300);
task.Wait();
Console.WriteLine("主线程结束");

//开启新任务的方法：Task.Run()或者Task.Factory.StartNew()，开启的是后台线程

//要在主线程中等待后台线程执行完毕，
//可以使用Wait方法(会以同步的方式来执行)。不用Wait则会以异步的方式来执行。

// Task<TResult>就是有返回值的Task，TResult就是返回值类型。


Console.WriteLine("主线程开始");
//返回值类型为string
Task<string> task = Task<string>.Run(() => {
    Thread.Sleep(2000); 
    return Thread.CurrentThread.ManagedThreadId.ToString(); 
});
//会等到task执行完毕才会输出;
Console.WriteLine(task.Result);
Console.WriteLine("主线程结束");


//6、async/await是C#5.0中推出的
tatic void Main(string[] args)
{
    Console.WriteLine("-------主线程启动-------");
    Task<int> task = GetStrLengthAsync();
    Console.WriteLine("主线程继续执行");
    Console.WriteLine("Task返回的值" + task.Result);
    Console.WriteLine("-------主线程结束-------");
}

static async Task<int> GetStrLengthAsync()
{
    Console.WriteLine("GetStrLengthAsync方法开始执行");
    //此处返回的<string>中的字符串类型，而不是Task<string>
    string str = await GetString();
    Console.WriteLine("GetStrLengthAsync方法执行结束");
    return str.Length;
}

static Task<string> GetString()
{
　　 //Console.WriteLine("GetString方法开始执行")
    return Task<string>.Run(() =>
    {
        Thread.Sleep(2000);
        return "GetString的返回值";
    });
}

// async用来修饰方法，表明这个方法是异步的，声明的方法的返回类型必须为：void，Task或Task<TResult>。

// await必须用来修饰Task或Task<TResult>，而且只能出现在已经用async关键字修饰的异步方法中。通常情况下，async/await成对出现才有意义，

//main函数调用GetStrLengthAsync方法后，在await之前，都是同步执行的，直到遇到await关键字，main函数才返回继续执行。

//7、IAsyncResult自.NET1.1起就有了，包含可异步操作的方法的类需要实现它，Task类就实现了该接口

