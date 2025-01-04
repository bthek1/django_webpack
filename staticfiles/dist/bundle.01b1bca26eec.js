/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./frontend/index.ts":
/*!***************************!*\
  !*** ./frontend/index.ts ***!
  \***************************/
/***/ (() => {

eval("\nconst todos = [];\nconst addTodo = (title) => {\n    todos.push({ title, completed: false });\n    renderTodos();\n};\nconst toggleTodo = (index) => {\n    todos[index].completed = !todos[index].completed;\n    renderTodos();\n};\nconst renderTodos = () => {\n    const todoList = document.getElementById('todo-list');\n    todoList.innerHTML = todos\n        .map((todo, index) => `\n                <li>\n                    <input type=\"checkbox\" ${todo.completed ? 'checked' : ''} onchange=\"toggle(${index})\" />\n                    ${todo.title}\n                </li>\n            `)\n        .join('');\n};\n// Attach global functions for simplicity\nwindow.addTodo = addTodo;\nwindow.toggle = toggleTodo;\n\n\n//# sourceURL=webpack://django_webpack/./frontend/index.ts?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./frontend/index.ts"]();
/******/ 	
/******/ })()
;