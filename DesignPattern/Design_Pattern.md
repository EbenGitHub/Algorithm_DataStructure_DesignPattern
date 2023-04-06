# Design Pattern

###

Design patterns are reusable solutions to common software design problems. They provide a way to solve problems that have been encountered and solved before, and can help you write more efficient, maintainable, and scalable code.

######

Design patterns are typically categorized into three main types: creational patterns, structural patterns, and behavioral patterns.

- **Creational patterns**: These patterns are used to create objects and classes in a flexible and reusable way. They provide a way to create objects without specifying the exact class of object that will be created. Examples of creational patterns include the Singleton pattern, Factory pattern, and Builder pattern.
- **Structural patterns**: These patterns are used to organize and structure classes and objects in a way that is easy to understand and maintain. They provide a way to create relationships between objects and classes, and to simplify complex structures. Examples of structural patterns include the Adapter pattern, Decorator pattern, and Facade pattern.
- **Behavioral patterns**: These patterns are used to manage the interactions and communication between objects and classes. They provide a way to define how objects and classes interact with each other, and to manage complex behaviors. Examples of behavioral patterns include the Observer pattern, Command pattern, and Strategy pattern.

######

Design patterns are typically described using a common vocabulary and notation, which makes them easy to understand and communicate. They are also often accompanied by code examples and diagrams, which illustrate how the pattern can be applied in practice.

Overall, learning about design patterns can help you write more efficient, maintainable, and scalable code, and is an important skill for any software developer. By understanding and applying design patterns, you can solve common software design problems in a flexible and reusable way, and create high-quality software that is easy to understand and maintain.

###

## Creational patterns

Creational design patterns are used to create objects and classes in a flexible and reusable way. They provide a way to create objects without specifying the exact class of object that will be created. This can be useful in situations where you want to create objects dynamically, or where you want to create objects based on certain conditions or parameters.

Here are some examples of creational design patterns:

- Singleton pattern: This pattern ensures that only one instance of a class is created, and provides a global point of access to that instance. This can be useful in situations where you want to ensure that only one instance of a class exists, such as a database connection or a configuration object.
- Factory pattern: This pattern provides a way to create objects without specifying the exact class of object that will be created. It uses a factory method to create objects based on certain conditions or parameters. This can be useful in situations where you want to create objects dynamically, or where you want to create objects based on user input or other external factors.
- Builder pattern: This pattern provides a way to create complex objects step-by-step, using a builder object. It allows you to create objects with different configurations and options, without having to create multiple constructors or subclasses. This can be useful in situations where you want to create objects with different configurations or options, such as a user profile or a product catalog.

######

1. **Singleton Pattern**:

```js
class DatabaseConnection {
  static #instance = null;

  static getInstance() {
    if (!DatabaseConnection.#instance) {
      DatabaseConnection.#instance = new DatabaseConnection();
    }
    return DatabaseConnection.#instance;
  }

  constructor() {
    if (DatabaseConnection.#instance) {
      throw new Error("Singleton class, use getInstance() method instead");
    }
    DatabaseConnection.#instance = this;
  }
}
```

> In this example, the DatabaseConnection class has a private #instance variable that holds the singleton instance. The getInstance() method returns the singleton instance, creating it if it doesn't exist yet.

2. **Factory Method Pattern**:

```js
class ShapeFactory {
  createShape(shapeType) {
    if (shapeType === "circle") {
      return new Circle();
    } else if (shapeType === "square") {
      return new Square();
    } else if (shapeType === "triangle") {
      return new Triangle();
    }
  }
}

class Circle {}
class Square {}
class Triangle {}
```

> In this example, the ShapeFactory class has a createShape() method that takes a shapeType parameter and returns an object of the corresponding class. The Circle, Square, and Triangle classes are the concrete classes that implement the Shape interface.

3. **Builder Pattern**:

```js
class Pizza {
  constructor(size, crust, toppings) {
    this.size = size;
    this.crust = crust;
    this.toppings = toppings;
  }
}

class PizzaBuilder {
  constructor() {
    this.size = null;
    this.crust = null;
    this.toppings = [];
  }

  setSize(size) {
    this.size = size;
    return this;
  }

  setCrust(crust) {
    this.crust = crust;
    return this;
  }

  addTopping(topping) {
    this.toppings.push(topping);
    return this;
  }

  build() {
    return new Pizza(this.size, this.crust, this.toppings);
  }
}
```

> In this example, the Pizza class has a constructor that takes a size, crust, and toppings parameter. The PizzaBuilder class has methods to set the size, crust, and toppings of the pizza, and a build() method that returns a Pizza object with the specified options. This allows you to create Pizza objects with different options without having to create a separate constructor for each combination of options.

###

## Structural patterns

Structural Design Patterns are concerned with the composition of classes and objects to form larger structures. These patterns focus on how objects are connected and how they work together to form larger structures.

Structural patterns are used to solve problems related to object composition, such as creating complex objects by combining simpler objects, or providing a simplified interface to a complex system.

Some examples of Structural Design Patterns include:

- Adapter Pattern: This pattern allows objects with incompatible interfaces to work together by creating a wrapper object that translates one interface to another.

- Decorator Pattern: This pattern allows you to add behavior to an object dynamically, without changing its interface.

- Facade Pattern: This pattern provides a simplified interface to a complex system, hiding its complexity from clients.

Each of these patterns provides a different way to structure the composition of objects in a manner suitable to the situation. By understanding the different structural patterns, developers can choose the appropriate pattern for their specific needs and improve the flexibility, extensibility, and maintainability of their software.

######

1. **Adapter Pattern**:
   The Adapter pattern allows incompatible interfaces to work together by creating a wrapper object that translates one interface to another. This pattern is useful when you need to use an existing class that doesn't quite fit with the rest of your code.

```js
class LegacyRectangle {
  constructor(x1, y1, x2, y2) {
    this.x1 = x1;
    this.y1 = y1;
    this.x2 = x2;
    this.y2 = y2;
  }

  draw() {
    console.log(
      `Drawing rectangle from (${this.x1},${this.y1}) to (${this.x2},${this.y2})`
    );
  }
}

class RectangleAdapter {
  constructor(x, y, width, height) {
    this.rectangle = new LegacyRectangle(x, y, x + width, y + height);
  }

  draw() {
    this.rectangle.draw();
  }
}

const rectangle = new RectangleAdapter(10, 10, 20, 30);
rectangle.draw();
```

> In this example, the LegacyRectangle class has an incompatible interface with the rest of the code. The RectangleAdapter class creates a wrapper object that translates the draw() method of the LegacyRectangle class to a compatible interface.

2. **Decorator Pattern**:
   The Decorator pattern allows you to add behavior to an object dynamically, without changing its interface. This pattern is useful when you want to add functionality to an object without changing its core functionality.

```js
class Component {
  operation() {}
}

class ConcreteComponent extends Component {
  operation() {
    console.log("ConcreteComponent operation");
  }
}

class Decorator extends Component {
  constructor(component) {
    super();
    this.component = component;
  }

  operation() {
    this.component.operation();
  }
}

class ConcreteDecoratorA extends Decorator {
  operation() {
    super.operation();
    console.log("ConcreteDecoratorA operation");
  }
}

class ConcreteDecoratorB extends Decorator {
  operation() {
    super.operation();
    console.log("ConcreteDecoratorB operation");
  }
}

const component = new ConcreteComponent();
const decoratorA = new ConcreteDecoratorA(component);
const decoratorB = new ConcreteDecoratorB(decoratorA);
decoratorB.operation();
```

> In this example, the Component class is the base class for both the ConcreteComponent and Decorator classes. The Decorator class has a reference to a Component object, allowing you to add behavior to the object dynamically.

3. **Facade Pattern**:
   The Facade pattern provides a simplified interface to a complex system, hiding its complexity from clients. This pattern is useful when you want to provide a simple interface to a complex system, so that clients don't need to know the details of how the system works.

```js
class SubsystemA {
  operationA() {
    console.log("SubsystemA operation");
  }
}

class SubsystemB {
  operationB() {
    console.log("SubsystemB operation");
  }
}

class Facade {
  constructor() {
    this.subsystemA = new SubsystemA();
    this.subsystemB = new SubsystemB();
  }

  operation() {
    this.subsystemA.operationA();
    this.subsystemB.operationB();
  }
}

const facade = new Facade();
facade.operation();
```

> In this example, the SubsystemA and SubsystemB classes are the complex system, and the Facade class provides a simplified interface to the system. Clients can use the Facade class to perform operations on the system without needing to know the details of how the system works.

###

## Behavioral patterns

Behavioral Design Patterns are concerned with the communication between objects, how objects collaborate and how they operate together to achieve a common goal. These patterns focus on the interaction between objects and the delegation of responsibilities among them.

Behavioral patterns are used to solve problems related to communication between objects, such as managing complex interactions between objects, defining algorithms and encapsulating requests.

Some examples of Behavioral Design Patterns include:

- Observer Pattern: This pattern defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.

- Strategy Pattern: This pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern allows you to change the algorithm used by an object at runtime.

- Command Pattern: This pattern encapsulates a request as an object, allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.

Each of these patterns provides a different way to structure the communication and collaboration between objects in a manner suitable to the situation. By understanding the different behavioral patterns, developers can choose the appropriate pattern for their specific needs and improve the flexibility, extensibility, and maintainability of their software.

######

1. **Observer Pattern**:
   The Observer pattern defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.

```js
class Subject {
  constructor() {
    this.observers = [];
  }

  addObserver(observer) {
    this.observers.push(observer);
  }

  removeObserver(observer) {
    const index = this.observers.indexOf(observer);
    if (index !== -1) {
      this.observers.splice(index, 1);
    }
  }

  notifyObservers() {
    for (const observer of this.observers) {
      observer.update();
    }
  }
}

class ConcreteSubject extends Subject {
  constructor() {
    super();
    this.state = 0;
  }

  getState() {
    return this.state;
  }

  setState(state) {
    this.state = state;
    this.notifyObservers();
  }
}

class Observer {
  update() {}
}

class ConcreteObserver extends Observer {
  constructor(subject) {
    super();
    this.subject = subject;
    this.subject.addObserver(this);
  }

  update() {
    console.log(
      `ConcreteObserver updated with state ${this.subject.getState()}`
    );
  }
}

const subject = new ConcreteSubject();
const observer1 = new ConcreteObserver(subject);
const observer2 = new ConcreteObserver(subject);
subject.setState(1);
subject.removeObserver(observer2);
subject.setState(2);
```

> In this example, the Subject class is the object that is being observed, and the Observer class is the object that is observing the subject. The ConcreteSubject class is a specific implementation of the Subject class, and the ConcreteObserver class is a specific implementation of the Observer class. When the state of the ConcreteSubject object changes, it notifies all its observers, which update themselves accordingly.

2. **Strategy Pattern**:
   The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern allows you to change the algorithm used by an object at runtime.

```js
class Context {
  constructor(strategy) {
    this.strategy = strategy;
  }

  setStrategy(strategy) {
    this.strategy = strategy;
  }

  executeStrategy() {
    this.strategy.execute();
  }
}

class Strategy {
  execute() {}
}

class ConcreteStrategyA extends Strategy {
  execute() {
    console.log("ConcreteStrategyA executed");
  }
}

class ConcreteStrategyB extends Strategy {
  execute() {
    console.log("ConcreteStrategyB executed");
  }
}

const context = new Context(new ConcreteStrategyA());
context.executeStrategy();
context.setStrategy(new ConcreteStrategyB());
context.executeStrategy();
```

> In this example, the Context class is the object that uses the strategy, and the Strategy class is the abstract base class for all strategies. The ConcreteStrategyA and ConcreteStrategyB classes are specific implementations of the Strategy class. The Context object can change its strategy at runtime by setting a new strategy object.

3. **Command Pattern**:
   The Command pattern encapsulates a request as an object, allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.

```js
class Receiver {
  action() {
    console.log("Receiver action");
  }
}

class Command {
  execute() {}
}

class ConcreteCommand extends Command {
  constructor(receiver) {
    super();
    this.receiver = receiver;
  }

  execute() {
    this.receiver.action();
  }
}

class Invoker {
  constructor() {
    this.commands = [];
  }

  addCommand(command) {
    this.commands.push(command);
  }

  executeCommands() {
    for (const command of this.commands) {
      command.execute();
    }
  }
}

const receiver = new Receiver();
const command = new ConcreteCommand(receiver);
const invoker = new Invoker();
invoker.addCommand(command);
invoker.executeCommands();
```

> In this example, the Receiver class is the object that performs the action, and the Command class is the abstract base class for all commands. The ConcreteCommand class is a specific implementation of the Command class that encapsulates a request to the Receiver object. The Invoker class is the object that invokes the command, and can queue or log commands for later execution.

######

Overall, creational design patterns provide a way to create objects and classes in a flexible and reusable way, and can help you write more efficient, maintainable, and scalable code. By understanding and applying creational design patterns, you can create high-quality software that is easy to understand and maintain.
