package com.soni.threadPool;

import java.util.LinkedList;
import java.util.Queue;

public class CustomThreadPool {
	public static void main(String[] args) {
		TheadPoolManager pool = new TheadPoolManager(2);
		pool.submitTask(()->{
			System.out.println("Executing task 1");
			try {
				Thread.sleep(2000);
			} catch (Exception e) {
				e.printStackTrace();
			}
			System.out.println("Finished task 1");
		});
		
		pool.submitTask(()->{
			System.out.println("Executing task 2");
			try {
				Thread.sleep(2000);
			} catch (Exception e) {
				e.printStackTrace();
			}
			System.out.println("Finished task 2");
		});
		
		pool.submitTask(()->{
			System.out.println("Executing task 3");
			try {
				Thread.sleep(2000);
			} catch (Exception e) {
				e.printStackTrace();
			}
			System.out.println("Finished task 3");
		});
	}
}

class TheadPoolManager {
	private CustomQueue<Runnable> queue;
	
	public TheadPoolManager(int nThreads) {
		 queue = new CustomQueue<Runnable>(nThreads);
		for(int i=0; i<nThreads; i++) {
			Thread t = new Thread(new ExecutionThread(queue));
			t.setName("Thread-"+(i+1));
			t.start();
		}
	}
	
	public void submitTask(Runnable runnable) {
		queue.enqueue(runnable);
	}
	
}

class ExecutionThread implements Runnable {
	private CustomQueue<Runnable> queue;
	
	public ExecutionThread(CustomQueue<Runnable> queue) {
		this.queue = queue;
	}
	
	public void run() {
		while(true) {
			queue.dequeue().run();
		}
	}
	
}

class CustomQueue<T> {
	private Queue<T> queue;
	private int capacity;
	
	public CustomQueue(int capacity) {
		this.queue = new LinkedList<T>();
		this.capacity = capacity;
	}
	
	public synchronized void enqueue(T elt) {
		if(queue.size()==capacity) {
			try {
				wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		queue.add(elt);
		notifyAll();
	}
	
	public synchronized T dequeue() {
		if(queue.isEmpty()) {
			try {
				wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		notifyAll();
		return queue.poll();
	}
}
