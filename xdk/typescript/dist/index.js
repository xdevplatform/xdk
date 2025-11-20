import { statSync, createReadStream, promises } from 'fs';
import { basename } from 'path';
import Stream, { pipeline as pipeline$1, PassThrough } from 'stream';
import { promisify, deprecate, types } from 'util';
import { Buffer as Buffer$1 } from 'buffer';
import http from 'http';
import { isIP } from 'net';
import { format } from 'url';
import https from 'https';
import zlib from 'zlib';

var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __require = /* @__PURE__ */ ((x2) => typeof require !== "undefined" ? require : typeof Proxy !== "undefined" ? new Proxy(x2, {
  get: (a, b) => (typeof require !== "undefined" ? require : a)[b]
}) : x2)(function(x2) {
  if (typeof require !== "undefined")
    return require.apply(this, arguments);
  throw Error('Dynamic require of "' + x2 + '" is not supported');
});
var __esm = (fn, res) => function __init() {
  return fn && (res = (0, fn[__getOwnPropNames(fn)[0]])(fn = 0)), res;
};
var __commonJS = (cb, mod) => function __require2() {
  return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
};
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// node_modules/data-uri-to-buffer/dist/index.js
function dataUriToBuffer(uri) {
  if (!/^data:/i.test(uri)) {
    throw new TypeError('`uri` does not appear to be a Data URI (must begin with "data:")');
  }
  uri = uri.replace(/\r?\n/g, "");
  const firstComma = uri.indexOf(",");
  if (firstComma === -1 || firstComma <= 4) {
    throw new TypeError("malformed data: URI");
  }
  const meta = uri.substring(5, firstComma).split(";");
  let charset = "";
  let base64 = false;
  const type = meta[0] || "text/plain";
  let typeFull = type;
  for (let i2 = 1; i2 < meta.length; i2++) {
    if (meta[i2] === "base64") {
      base64 = true;
    } else if (meta[i2]) {
      typeFull += `;${meta[i2]}`;
      if (meta[i2].indexOf("charset=") === 0) {
        charset = meta[i2].substring(8);
      }
    }
  }
  if (!meta[0] && !charset.length) {
    typeFull += ";charset=US-ASCII";
    charset = "US-ASCII";
  }
  const encoding = base64 ? "base64" : "ascii";
  const data = unescape(uri.substring(firstComma + 1));
  const buffer = Buffer.from(data, encoding);
  buffer.type = type;
  buffer.typeFull = typeFull;
  buffer.charset = charset;
  return buffer;
}
var dist_default;
var init_dist = __esm({
  "node_modules/data-uri-to-buffer/dist/index.js"() {
    dist_default = dataUriToBuffer;
  }
});

// node_modules/web-streams-polyfill/dist/ponyfill.es2018.js
var require_ponyfill_es2018 = __commonJS({
  "node_modules/web-streams-polyfill/dist/ponyfill.es2018.js"(exports, module) {
    (function(global2, factory) {
      typeof exports === "object" && typeof module !== "undefined" ? factory(exports) : typeof define === "function" && define.amd ? define(["exports"], factory) : (global2 = typeof globalThis !== "undefined" ? globalThis : global2 || self, factory(global2.WebStreamsPolyfill = {}));
    })(exports, function(exports2) {
      function noop2() {
        return void 0;
      }
      function typeIsObject(x2) {
        return typeof x2 === "object" && x2 !== null || typeof x2 === "function";
      }
      const rethrowAssertionErrorRejection = noop2;
      function setFunctionName(fn, name) {
        try {
          Object.defineProperty(fn, "name", {
            value: name,
            configurable: true
          });
        } catch (_a2) {
        }
      }
      const originalPromise = Promise;
      const originalPromiseThen = Promise.prototype.then;
      const originalPromiseReject = Promise.reject.bind(originalPromise);
      function newPromise(executor) {
        return new originalPromise(executor);
      }
      function promiseResolvedWith(value) {
        return newPromise((resolve) => resolve(value));
      }
      function promiseRejectedWith(reason) {
        return originalPromiseReject(reason);
      }
      function PerformPromiseThen(promise, onFulfilled, onRejected) {
        return originalPromiseThen.call(promise, onFulfilled, onRejected);
      }
      function uponPromise(promise, onFulfilled, onRejected) {
        PerformPromiseThen(PerformPromiseThen(promise, onFulfilled, onRejected), void 0, rethrowAssertionErrorRejection);
      }
      function uponFulfillment(promise, onFulfilled) {
        uponPromise(promise, onFulfilled);
      }
      function uponRejection(promise, onRejected) {
        uponPromise(promise, void 0, onRejected);
      }
      function transformPromiseWith(promise, fulfillmentHandler, rejectionHandler) {
        return PerformPromiseThen(promise, fulfillmentHandler, rejectionHandler);
      }
      function setPromiseIsHandledToTrue(promise) {
        PerformPromiseThen(promise, void 0, rethrowAssertionErrorRejection);
      }
      let _queueMicrotask = (callback) => {
        if (typeof queueMicrotask === "function") {
          _queueMicrotask = queueMicrotask;
        } else {
          const resolvedPromise = promiseResolvedWith(void 0);
          _queueMicrotask = (cb) => PerformPromiseThen(resolvedPromise, cb);
        }
        return _queueMicrotask(callback);
      };
      function reflectCall(F2, V, args) {
        if (typeof F2 !== "function") {
          throw new TypeError("Argument is not a function");
        }
        return Function.prototype.apply.call(F2, V, args);
      }
      function promiseCall(F2, V, args) {
        try {
          return promiseResolvedWith(reflectCall(F2, V, args));
        } catch (value) {
          return promiseRejectedWith(value);
        }
      }
      const QUEUE_MAX_ARRAY_SIZE = 16384;
      class SimpleQueue {
        constructor() {
          this._cursor = 0;
          this._size = 0;
          this._front = {
            _elements: [],
            _next: void 0
          };
          this._back = this._front;
          this._cursor = 0;
          this._size = 0;
        }
        get length() {
          return this._size;
        }
        // For exception safety, this method is structured in order:
        // 1. Read state
        // 2. Calculate required state mutations
        // 3. Perform state mutations
        push(element) {
          const oldBack = this._back;
          let newBack = oldBack;
          if (oldBack._elements.length === QUEUE_MAX_ARRAY_SIZE - 1) {
            newBack = {
              _elements: [],
              _next: void 0
            };
          }
          oldBack._elements.push(element);
          if (newBack !== oldBack) {
            this._back = newBack;
            oldBack._next = newBack;
          }
          ++this._size;
        }
        // Like push(), shift() follows the read -> calculate -> mutate pattern for
        // exception safety.
        shift() {
          const oldFront = this._front;
          let newFront = oldFront;
          const oldCursor = this._cursor;
          let newCursor = oldCursor + 1;
          const elements = oldFront._elements;
          const element = elements[oldCursor];
          if (newCursor === QUEUE_MAX_ARRAY_SIZE) {
            newFront = oldFront._next;
            newCursor = 0;
          }
          --this._size;
          this._cursor = newCursor;
          if (oldFront !== newFront) {
            this._front = newFront;
          }
          elements[oldCursor] = void 0;
          return element;
        }
        // The tricky thing about forEach() is that it can be called
        // re-entrantly. The queue may be mutated inside the callback. It is easy to
        // see that push() within the callback has no negative effects since the end
        // of the queue is checked for on every iteration. If shift() is called
        // repeatedly within the callback then the next iteration may return an
        // element that has been removed. In this case the callback will be called
        // with undefined values until we either "catch up" with elements that still
        // exist or reach the back of the queue.
        forEach(callback) {
          let i2 = this._cursor;
          let node = this._front;
          let elements = node._elements;
          while (i2 !== elements.length || node._next !== void 0) {
            if (i2 === elements.length) {
              node = node._next;
              elements = node._elements;
              i2 = 0;
              if (elements.length === 0) {
                break;
              }
            }
            callback(elements[i2]);
            ++i2;
          }
        }
        // Return the element that would be returned if shift() was called now,
        // without modifying the queue.
        peek() {
          const front = this._front;
          const cursor = this._cursor;
          return front._elements[cursor];
        }
      }
      const AbortSteps = Symbol("[[AbortSteps]]");
      const ErrorSteps = Symbol("[[ErrorSteps]]");
      const CancelSteps = Symbol("[[CancelSteps]]");
      const PullSteps = Symbol("[[PullSteps]]");
      const ReleaseSteps = Symbol("[[ReleaseSteps]]");
      function ReadableStreamReaderGenericInitialize(reader, stream) {
        reader._ownerReadableStream = stream;
        stream._reader = reader;
        if (stream._state === "readable") {
          defaultReaderClosedPromiseInitialize(reader);
        } else if (stream._state === "closed") {
          defaultReaderClosedPromiseInitializeAsResolved(reader);
        } else {
          defaultReaderClosedPromiseInitializeAsRejected(reader, stream._storedError);
        }
      }
      function ReadableStreamReaderGenericCancel(reader, reason) {
        const stream = reader._ownerReadableStream;
        return ReadableStreamCancel(stream, reason);
      }
      function ReadableStreamReaderGenericRelease(reader) {
        const stream = reader._ownerReadableStream;
        if (stream._state === "readable") {
          defaultReaderClosedPromiseReject(reader, new TypeError(`Reader was released and can no longer be used to monitor the stream's closedness`));
        } else {
          defaultReaderClosedPromiseResetToRejected(reader, new TypeError(`Reader was released and can no longer be used to monitor the stream's closedness`));
        }
        stream._readableStreamController[ReleaseSteps]();
        stream._reader = void 0;
        reader._ownerReadableStream = void 0;
      }
      function readerLockException(name) {
        return new TypeError("Cannot " + name + " a stream using a released reader");
      }
      function defaultReaderClosedPromiseInitialize(reader) {
        reader._closedPromise = newPromise((resolve, reject) => {
          reader._closedPromise_resolve = resolve;
          reader._closedPromise_reject = reject;
        });
      }
      function defaultReaderClosedPromiseInitializeAsRejected(reader, reason) {
        defaultReaderClosedPromiseInitialize(reader);
        defaultReaderClosedPromiseReject(reader, reason);
      }
      function defaultReaderClosedPromiseInitializeAsResolved(reader) {
        defaultReaderClosedPromiseInitialize(reader);
        defaultReaderClosedPromiseResolve(reader);
      }
      function defaultReaderClosedPromiseReject(reader, reason) {
        if (reader._closedPromise_reject === void 0) {
          return;
        }
        setPromiseIsHandledToTrue(reader._closedPromise);
        reader._closedPromise_reject(reason);
        reader._closedPromise_resolve = void 0;
        reader._closedPromise_reject = void 0;
      }
      function defaultReaderClosedPromiseResetToRejected(reader, reason) {
        defaultReaderClosedPromiseInitializeAsRejected(reader, reason);
      }
      function defaultReaderClosedPromiseResolve(reader) {
        if (reader._closedPromise_resolve === void 0) {
          return;
        }
        reader._closedPromise_resolve(void 0);
        reader._closedPromise_resolve = void 0;
        reader._closedPromise_reject = void 0;
      }
      const NumberIsFinite = Number.isFinite || function(x2) {
        return typeof x2 === "number" && isFinite(x2);
      };
      const MathTrunc = Math.trunc || function(v) {
        return v < 0 ? Math.ceil(v) : Math.floor(v);
      };
      function isDictionary(x2) {
        return typeof x2 === "object" || typeof x2 === "function";
      }
      function assertDictionary(obj, context) {
        if (obj !== void 0 && !isDictionary(obj)) {
          throw new TypeError(`${context} is not an object.`);
        }
      }
      function assertFunction(x2, context) {
        if (typeof x2 !== "function") {
          throw new TypeError(`${context} is not a function.`);
        }
      }
      function isObject(x2) {
        return typeof x2 === "object" && x2 !== null || typeof x2 === "function";
      }
      function assertObject(x2, context) {
        if (!isObject(x2)) {
          throw new TypeError(`${context} is not an object.`);
        }
      }
      function assertRequiredArgument(x2, position, context) {
        if (x2 === void 0) {
          throw new TypeError(`Parameter ${position} is required in '${context}'.`);
        }
      }
      function assertRequiredField(x2, field, context) {
        if (x2 === void 0) {
          throw new TypeError(`${field} is required in '${context}'.`);
        }
      }
      function convertUnrestrictedDouble(value) {
        return Number(value);
      }
      function censorNegativeZero(x2) {
        return x2 === 0 ? 0 : x2;
      }
      function integerPart(x2) {
        return censorNegativeZero(MathTrunc(x2));
      }
      function convertUnsignedLongLongWithEnforceRange(value, context) {
        const lowerBound = 0;
        const upperBound = Number.MAX_SAFE_INTEGER;
        let x2 = Number(value);
        x2 = censorNegativeZero(x2);
        if (!NumberIsFinite(x2)) {
          throw new TypeError(`${context} is not a finite number`);
        }
        x2 = integerPart(x2);
        if (x2 < lowerBound || x2 > upperBound) {
          throw new TypeError(`${context} is outside the accepted range of ${lowerBound} to ${upperBound}, inclusive`);
        }
        if (!NumberIsFinite(x2) || x2 === 0) {
          return 0;
        }
        return x2;
      }
      function assertReadableStream(x2, context) {
        if (!IsReadableStream(x2)) {
          throw new TypeError(`${context} is not a ReadableStream.`);
        }
      }
      function AcquireReadableStreamDefaultReader(stream) {
        return new ReadableStreamDefaultReader(stream);
      }
      function ReadableStreamAddReadRequest(stream, readRequest) {
        stream._reader._readRequests.push(readRequest);
      }
      function ReadableStreamFulfillReadRequest(stream, chunk, done) {
        const reader = stream._reader;
        const readRequest = reader._readRequests.shift();
        if (done) {
          readRequest._closeSteps();
        } else {
          readRequest._chunkSteps(chunk);
        }
      }
      function ReadableStreamGetNumReadRequests(stream) {
        return stream._reader._readRequests.length;
      }
      function ReadableStreamHasDefaultReader(stream) {
        const reader = stream._reader;
        if (reader === void 0) {
          return false;
        }
        if (!IsReadableStreamDefaultReader(reader)) {
          return false;
        }
        return true;
      }
      class ReadableStreamDefaultReader {
        constructor(stream) {
          assertRequiredArgument(stream, 1, "ReadableStreamDefaultReader");
          assertReadableStream(stream, "First parameter");
          if (IsReadableStreamLocked(stream)) {
            throw new TypeError("This stream has already been locked for exclusive reading by another reader");
          }
          ReadableStreamReaderGenericInitialize(this, stream);
          this._readRequests = new SimpleQueue();
        }
        /**
         * Returns a promise that will be fulfilled when the stream becomes closed,
         * or rejected if the stream ever errors or the reader's lock is released before the stream finishes closing.
         */
        get closed() {
          if (!IsReadableStreamDefaultReader(this)) {
            return promiseRejectedWith(defaultReaderBrandCheckException("closed"));
          }
          return this._closedPromise;
        }
        /**
         * If the reader is active, behaves the same as {@link ReadableStream.cancel | stream.cancel(reason)}.
         */
        cancel(reason = void 0) {
          if (!IsReadableStreamDefaultReader(this)) {
            return promiseRejectedWith(defaultReaderBrandCheckException("cancel"));
          }
          if (this._ownerReadableStream === void 0) {
            return promiseRejectedWith(readerLockException("cancel"));
          }
          return ReadableStreamReaderGenericCancel(this, reason);
        }
        /**
         * Returns a promise that allows access to the next chunk from the stream's internal queue, if available.
         *
         * If reading a chunk causes the queue to become empty, more data will be pulled from the underlying source.
         */
        read() {
          if (!IsReadableStreamDefaultReader(this)) {
            return promiseRejectedWith(defaultReaderBrandCheckException("read"));
          }
          if (this._ownerReadableStream === void 0) {
            return promiseRejectedWith(readerLockException("read from"));
          }
          let resolvePromise;
          let rejectPromise;
          const promise = newPromise((resolve, reject) => {
            resolvePromise = resolve;
            rejectPromise = reject;
          });
          const readRequest = {
            _chunkSteps: (chunk) => resolvePromise({ value: chunk, done: false }),
            _closeSteps: () => resolvePromise({ value: void 0, done: true }),
            _errorSteps: (e2) => rejectPromise(e2)
          };
          ReadableStreamDefaultReaderRead(this, readRequest);
          return promise;
        }
        /**
         * Releases the reader's lock on the corresponding stream. After the lock is released, the reader is no longer active.
         * If the associated stream is errored when the lock is released, the reader will appear errored in the same way
         * from now on; otherwise, the reader will appear closed.
         *
         * A reader's lock cannot be released while it still has a pending read request, i.e., if a promise returned by
         * the reader's {@link ReadableStreamDefaultReader.read | read()} method has not yet been settled. Attempting to
         * do so will throw a `TypeError` and leave the reader locked to the stream.
         */
        releaseLock() {
          if (!IsReadableStreamDefaultReader(this)) {
            throw defaultReaderBrandCheckException("releaseLock");
          }
          if (this._ownerReadableStream === void 0) {
            return;
          }
          ReadableStreamDefaultReaderRelease(this);
        }
      }
      Object.defineProperties(ReadableStreamDefaultReader.prototype, {
        cancel: { enumerable: true },
        read: { enumerable: true },
        releaseLock: { enumerable: true },
        closed: { enumerable: true }
      });
      setFunctionName(ReadableStreamDefaultReader.prototype.cancel, "cancel");
      setFunctionName(ReadableStreamDefaultReader.prototype.read, "read");
      setFunctionName(ReadableStreamDefaultReader.prototype.releaseLock, "releaseLock");
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(ReadableStreamDefaultReader.prototype, Symbol.toStringTag, {
          value: "ReadableStreamDefaultReader",
          configurable: true
        });
      }
      function IsReadableStreamDefaultReader(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_readRequests")) {
          return false;
        }
        return x2 instanceof ReadableStreamDefaultReader;
      }
      function ReadableStreamDefaultReaderRead(reader, readRequest) {
        const stream = reader._ownerReadableStream;
        stream._disturbed = true;
        if (stream._state === "closed") {
          readRequest._closeSteps();
        } else if (stream._state === "errored") {
          readRequest._errorSteps(stream._storedError);
        } else {
          stream._readableStreamController[PullSteps](readRequest);
        }
      }
      function ReadableStreamDefaultReaderRelease(reader) {
        ReadableStreamReaderGenericRelease(reader);
        const e2 = new TypeError("Reader was released");
        ReadableStreamDefaultReaderErrorReadRequests(reader, e2);
      }
      function ReadableStreamDefaultReaderErrorReadRequests(reader, e2) {
        const readRequests = reader._readRequests;
        reader._readRequests = new SimpleQueue();
        readRequests.forEach((readRequest) => {
          readRequest._errorSteps(e2);
        });
      }
      function defaultReaderBrandCheckException(name) {
        return new TypeError(`ReadableStreamDefaultReader.prototype.${name} can only be used on a ReadableStreamDefaultReader`);
      }
      const AsyncIteratorPrototype = Object.getPrototypeOf(Object.getPrototypeOf(async function* () {
      }).prototype);
      class ReadableStreamAsyncIteratorImpl {
        constructor(reader, preventCancel) {
          this._ongoingPromise = void 0;
          this._isFinished = false;
          this._reader = reader;
          this._preventCancel = preventCancel;
        }
        next() {
          const nextSteps = () => this._nextSteps();
          this._ongoingPromise = this._ongoingPromise ? transformPromiseWith(this._ongoingPromise, nextSteps, nextSteps) : nextSteps();
          return this._ongoingPromise;
        }
        return(value) {
          const returnSteps = () => this._returnSteps(value);
          return this._ongoingPromise ? transformPromiseWith(this._ongoingPromise, returnSteps, returnSteps) : returnSteps();
        }
        _nextSteps() {
          if (this._isFinished) {
            return Promise.resolve({ value: void 0, done: true });
          }
          const reader = this._reader;
          let resolvePromise;
          let rejectPromise;
          const promise = newPromise((resolve, reject) => {
            resolvePromise = resolve;
            rejectPromise = reject;
          });
          const readRequest = {
            _chunkSteps: (chunk) => {
              this._ongoingPromise = void 0;
              _queueMicrotask(() => resolvePromise({ value: chunk, done: false }));
            },
            _closeSteps: () => {
              this._ongoingPromise = void 0;
              this._isFinished = true;
              ReadableStreamReaderGenericRelease(reader);
              resolvePromise({ value: void 0, done: true });
            },
            _errorSteps: (reason) => {
              this._ongoingPromise = void 0;
              this._isFinished = true;
              ReadableStreamReaderGenericRelease(reader);
              rejectPromise(reason);
            }
          };
          ReadableStreamDefaultReaderRead(reader, readRequest);
          return promise;
        }
        _returnSteps(value) {
          if (this._isFinished) {
            return Promise.resolve({ value, done: true });
          }
          this._isFinished = true;
          const reader = this._reader;
          if (!this._preventCancel) {
            const result = ReadableStreamReaderGenericCancel(reader, value);
            ReadableStreamReaderGenericRelease(reader);
            return transformPromiseWith(result, () => ({ value, done: true }));
          }
          ReadableStreamReaderGenericRelease(reader);
          return promiseResolvedWith({ value, done: true });
        }
      }
      const ReadableStreamAsyncIteratorPrototype = {
        next() {
          if (!IsReadableStreamAsyncIterator(this)) {
            return promiseRejectedWith(streamAsyncIteratorBrandCheckException("next"));
          }
          return this._asyncIteratorImpl.next();
        },
        return(value) {
          if (!IsReadableStreamAsyncIterator(this)) {
            return promiseRejectedWith(streamAsyncIteratorBrandCheckException("return"));
          }
          return this._asyncIteratorImpl.return(value);
        }
      };
      Object.setPrototypeOf(ReadableStreamAsyncIteratorPrototype, AsyncIteratorPrototype);
      function AcquireReadableStreamAsyncIterator(stream, preventCancel) {
        const reader = AcquireReadableStreamDefaultReader(stream);
        const impl = new ReadableStreamAsyncIteratorImpl(reader, preventCancel);
        const iterator = Object.create(ReadableStreamAsyncIteratorPrototype);
        iterator._asyncIteratorImpl = impl;
        return iterator;
      }
      function IsReadableStreamAsyncIterator(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_asyncIteratorImpl")) {
          return false;
        }
        try {
          return x2._asyncIteratorImpl instanceof ReadableStreamAsyncIteratorImpl;
        } catch (_a2) {
          return false;
        }
      }
      function streamAsyncIteratorBrandCheckException(name) {
        return new TypeError(`ReadableStreamAsyncIterator.${name} can only be used on a ReadableSteamAsyncIterator`);
      }
      const NumberIsNaN = Number.isNaN || function(x2) {
        return x2 !== x2;
      };
      var _a, _b, _c;
      function CreateArrayFromList(elements) {
        return elements.slice();
      }
      function CopyDataBlockBytes(dest, destOffset, src, srcOffset, n) {
        new Uint8Array(dest).set(new Uint8Array(src, srcOffset, n), destOffset);
      }
      let TransferArrayBuffer = (O) => {
        if (typeof O.transfer === "function") {
          TransferArrayBuffer = (buffer) => buffer.transfer();
        } else if (typeof structuredClone === "function") {
          TransferArrayBuffer = (buffer) => structuredClone(buffer, { transfer: [buffer] });
        } else {
          TransferArrayBuffer = (buffer) => buffer;
        }
        return TransferArrayBuffer(O);
      };
      let IsDetachedBuffer = (O) => {
        if (typeof O.detached === "boolean") {
          IsDetachedBuffer = (buffer) => buffer.detached;
        } else {
          IsDetachedBuffer = (buffer) => buffer.byteLength === 0;
        }
        return IsDetachedBuffer(O);
      };
      function ArrayBufferSlice(buffer, begin, end) {
        if (buffer.slice) {
          return buffer.slice(begin, end);
        }
        const length = end - begin;
        const slice = new ArrayBuffer(length);
        CopyDataBlockBytes(slice, 0, buffer, begin, length);
        return slice;
      }
      function GetMethod(receiver, prop) {
        const func = receiver[prop];
        if (func === void 0 || func === null) {
          return void 0;
        }
        if (typeof func !== "function") {
          throw new TypeError(`${String(prop)} is not a function`);
        }
        return func;
      }
      function CreateAsyncFromSyncIterator(syncIteratorRecord) {
        const syncIterable = {
          [Symbol.iterator]: () => syncIteratorRecord.iterator
        };
        const asyncIterator = async function* () {
          return yield* syncIterable;
        }();
        const nextMethod = asyncIterator.next;
        return { iterator: asyncIterator, nextMethod, done: false };
      }
      const SymbolAsyncIterator = (_c = (_a = Symbol.asyncIterator) !== null && _a !== void 0 ? _a : (_b = Symbol.for) === null || _b === void 0 ? void 0 : _b.call(Symbol, "Symbol.asyncIterator")) !== null && _c !== void 0 ? _c : "@@asyncIterator";
      function GetIterator(obj, hint = "sync", method) {
        if (method === void 0) {
          if (hint === "async") {
            method = GetMethod(obj, SymbolAsyncIterator);
            if (method === void 0) {
              const syncMethod = GetMethod(obj, Symbol.iterator);
              const syncIteratorRecord = GetIterator(obj, "sync", syncMethod);
              return CreateAsyncFromSyncIterator(syncIteratorRecord);
            }
          } else {
            method = GetMethod(obj, Symbol.iterator);
          }
        }
        if (method === void 0) {
          throw new TypeError("The object is not iterable");
        }
        const iterator = reflectCall(method, obj, []);
        if (!typeIsObject(iterator)) {
          throw new TypeError("The iterator method must return an object");
        }
        const nextMethod = iterator.next;
        return { iterator, nextMethod, done: false };
      }
      function IteratorNext(iteratorRecord) {
        const result = reflectCall(iteratorRecord.nextMethod, iteratorRecord.iterator, []);
        if (!typeIsObject(result)) {
          throw new TypeError("The iterator.next() method must return an object");
        }
        return result;
      }
      function IteratorComplete(iterResult) {
        return Boolean(iterResult.done);
      }
      function IteratorValue(iterResult) {
        return iterResult.value;
      }
      function IsNonNegativeNumber(v) {
        if (typeof v !== "number") {
          return false;
        }
        if (NumberIsNaN(v)) {
          return false;
        }
        if (v < 0) {
          return false;
        }
        return true;
      }
      function CloneAsUint8Array(O) {
        const buffer = ArrayBufferSlice(O.buffer, O.byteOffset, O.byteOffset + O.byteLength);
        return new Uint8Array(buffer);
      }
      function DequeueValue(container) {
        const pair = container._queue.shift();
        container._queueTotalSize -= pair.size;
        if (container._queueTotalSize < 0) {
          container._queueTotalSize = 0;
        }
        return pair.value;
      }
      function EnqueueValueWithSize(container, value, size) {
        if (!IsNonNegativeNumber(size) || size === Infinity) {
          throw new RangeError("Size must be a finite, non-NaN, non-negative number.");
        }
        container._queue.push({ value, size });
        container._queueTotalSize += size;
      }
      function PeekQueueValue(container) {
        const pair = container._queue.peek();
        return pair.value;
      }
      function ResetQueue(container) {
        container._queue = new SimpleQueue();
        container._queueTotalSize = 0;
      }
      function isDataViewConstructor(ctor) {
        return ctor === DataView;
      }
      function isDataView(view) {
        return isDataViewConstructor(view.constructor);
      }
      function arrayBufferViewElementSize(ctor) {
        if (isDataViewConstructor(ctor)) {
          return 1;
        }
        return ctor.BYTES_PER_ELEMENT;
      }
      class ReadableStreamBYOBRequest {
        constructor() {
          throw new TypeError("Illegal constructor");
        }
        /**
         * Returns the view for writing in to, or `null` if the BYOB request has already been responded to.
         */
        get view() {
          if (!IsReadableStreamBYOBRequest(this)) {
            throw byobRequestBrandCheckException("view");
          }
          return this._view;
        }
        respond(bytesWritten) {
          if (!IsReadableStreamBYOBRequest(this)) {
            throw byobRequestBrandCheckException("respond");
          }
          assertRequiredArgument(bytesWritten, 1, "respond");
          bytesWritten = convertUnsignedLongLongWithEnforceRange(bytesWritten, "First parameter");
          if (this._associatedReadableByteStreamController === void 0) {
            throw new TypeError("This BYOB request has been invalidated");
          }
          if (IsDetachedBuffer(this._view.buffer)) {
            throw new TypeError(`The BYOB request's buffer has been detached and so cannot be used as a response`);
          }
          ReadableByteStreamControllerRespond(this._associatedReadableByteStreamController, bytesWritten);
        }
        respondWithNewView(view) {
          if (!IsReadableStreamBYOBRequest(this)) {
            throw byobRequestBrandCheckException("respondWithNewView");
          }
          assertRequiredArgument(view, 1, "respondWithNewView");
          if (!ArrayBuffer.isView(view)) {
            throw new TypeError("You can only respond with array buffer views");
          }
          if (this._associatedReadableByteStreamController === void 0) {
            throw new TypeError("This BYOB request has been invalidated");
          }
          if (IsDetachedBuffer(view.buffer)) {
            throw new TypeError("The given view's buffer has been detached and so cannot be used as a response");
          }
          ReadableByteStreamControllerRespondWithNewView(this._associatedReadableByteStreamController, view);
        }
      }
      Object.defineProperties(ReadableStreamBYOBRequest.prototype, {
        respond: { enumerable: true },
        respondWithNewView: { enumerable: true },
        view: { enumerable: true }
      });
      setFunctionName(ReadableStreamBYOBRequest.prototype.respond, "respond");
      setFunctionName(ReadableStreamBYOBRequest.prototype.respondWithNewView, "respondWithNewView");
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(ReadableStreamBYOBRequest.prototype, Symbol.toStringTag, {
          value: "ReadableStreamBYOBRequest",
          configurable: true
        });
      }
      class ReadableByteStreamController {
        constructor() {
          throw new TypeError("Illegal constructor");
        }
        /**
         * Returns the current BYOB pull request, or `null` if there isn't one.
         */
        get byobRequest() {
          if (!IsReadableByteStreamController(this)) {
            throw byteStreamControllerBrandCheckException("byobRequest");
          }
          return ReadableByteStreamControllerGetBYOBRequest(this);
        }
        /**
         * Returns the desired size to fill the controlled stream's internal queue. It can be negative, if the queue is
         * over-full. An underlying byte source ought to use this information to determine when and how to apply backpressure.
         */
        get desiredSize() {
          if (!IsReadableByteStreamController(this)) {
            throw byteStreamControllerBrandCheckException("desiredSize");
          }
          return ReadableByteStreamControllerGetDesiredSize(this);
        }
        /**
         * Closes the controlled readable stream. Consumers will still be able to read any previously-enqueued chunks from
         * the stream, but once those are read, the stream will become closed.
         */
        close() {
          if (!IsReadableByteStreamController(this)) {
            throw byteStreamControllerBrandCheckException("close");
          }
          if (this._closeRequested) {
            throw new TypeError("The stream has already been closed; do not close it again!");
          }
          const state = this._controlledReadableByteStream._state;
          if (state !== "readable") {
            throw new TypeError(`The stream (in ${state} state) is not in the readable state and cannot be closed`);
          }
          ReadableByteStreamControllerClose(this);
        }
        enqueue(chunk) {
          if (!IsReadableByteStreamController(this)) {
            throw byteStreamControllerBrandCheckException("enqueue");
          }
          assertRequiredArgument(chunk, 1, "enqueue");
          if (!ArrayBuffer.isView(chunk)) {
            throw new TypeError("chunk must be an array buffer view");
          }
          if (chunk.byteLength === 0) {
            throw new TypeError("chunk must have non-zero byteLength");
          }
          if (chunk.buffer.byteLength === 0) {
            throw new TypeError(`chunk's buffer must have non-zero byteLength`);
          }
          if (this._closeRequested) {
            throw new TypeError("stream is closed or draining");
          }
          const state = this._controlledReadableByteStream._state;
          if (state !== "readable") {
            throw new TypeError(`The stream (in ${state} state) is not in the readable state and cannot be enqueued to`);
          }
          ReadableByteStreamControllerEnqueue(this, chunk);
        }
        /**
         * Errors the controlled readable stream, making all future interactions with it fail with the given error `e`.
         */
        error(e2 = void 0) {
          if (!IsReadableByteStreamController(this)) {
            throw byteStreamControllerBrandCheckException("error");
          }
          ReadableByteStreamControllerError(this, e2);
        }
        /** @internal */
        [CancelSteps](reason) {
          ReadableByteStreamControllerClearPendingPullIntos(this);
          ResetQueue(this);
          const result = this._cancelAlgorithm(reason);
          ReadableByteStreamControllerClearAlgorithms(this);
          return result;
        }
        /** @internal */
        [PullSteps](readRequest) {
          const stream = this._controlledReadableByteStream;
          if (this._queueTotalSize > 0) {
            ReadableByteStreamControllerFillReadRequestFromQueue(this, readRequest);
            return;
          }
          const autoAllocateChunkSize = this._autoAllocateChunkSize;
          if (autoAllocateChunkSize !== void 0) {
            let buffer;
            try {
              buffer = new ArrayBuffer(autoAllocateChunkSize);
            } catch (bufferE) {
              readRequest._errorSteps(bufferE);
              return;
            }
            const pullIntoDescriptor = {
              buffer,
              bufferByteLength: autoAllocateChunkSize,
              byteOffset: 0,
              byteLength: autoAllocateChunkSize,
              bytesFilled: 0,
              minimumFill: 1,
              elementSize: 1,
              viewConstructor: Uint8Array,
              readerType: "default"
            };
            this._pendingPullIntos.push(pullIntoDescriptor);
          }
          ReadableStreamAddReadRequest(stream, readRequest);
          ReadableByteStreamControllerCallPullIfNeeded(this);
        }
        /** @internal */
        [ReleaseSteps]() {
          if (this._pendingPullIntos.length > 0) {
            const firstPullInto = this._pendingPullIntos.peek();
            firstPullInto.readerType = "none";
            this._pendingPullIntos = new SimpleQueue();
            this._pendingPullIntos.push(firstPullInto);
          }
        }
      }
      Object.defineProperties(ReadableByteStreamController.prototype, {
        close: { enumerable: true },
        enqueue: { enumerable: true },
        error: { enumerable: true },
        byobRequest: { enumerable: true },
        desiredSize: { enumerable: true }
      });
      setFunctionName(ReadableByteStreamController.prototype.close, "close");
      setFunctionName(ReadableByteStreamController.prototype.enqueue, "enqueue");
      setFunctionName(ReadableByteStreamController.prototype.error, "error");
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(ReadableByteStreamController.prototype, Symbol.toStringTag, {
          value: "ReadableByteStreamController",
          configurable: true
        });
      }
      function IsReadableByteStreamController(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_controlledReadableByteStream")) {
          return false;
        }
        return x2 instanceof ReadableByteStreamController;
      }
      function IsReadableStreamBYOBRequest(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_associatedReadableByteStreamController")) {
          return false;
        }
        return x2 instanceof ReadableStreamBYOBRequest;
      }
      function ReadableByteStreamControllerCallPullIfNeeded(controller) {
        const shouldPull = ReadableByteStreamControllerShouldCallPull(controller);
        if (!shouldPull) {
          return;
        }
        if (controller._pulling) {
          controller._pullAgain = true;
          return;
        }
        controller._pulling = true;
        const pullPromise = controller._pullAlgorithm();
        uponPromise(pullPromise, () => {
          controller._pulling = false;
          if (controller._pullAgain) {
            controller._pullAgain = false;
            ReadableByteStreamControllerCallPullIfNeeded(controller);
          }
          return null;
        }, (e2) => {
          ReadableByteStreamControllerError(controller, e2);
          return null;
        });
      }
      function ReadableByteStreamControllerClearPendingPullIntos(controller) {
        ReadableByteStreamControllerInvalidateBYOBRequest(controller);
        controller._pendingPullIntos = new SimpleQueue();
      }
      function ReadableByteStreamControllerCommitPullIntoDescriptor(stream, pullIntoDescriptor) {
        let done = false;
        if (stream._state === "closed") {
          done = true;
        }
        const filledView = ReadableByteStreamControllerConvertPullIntoDescriptor(pullIntoDescriptor);
        if (pullIntoDescriptor.readerType === "default") {
          ReadableStreamFulfillReadRequest(stream, filledView, done);
        } else {
          ReadableStreamFulfillReadIntoRequest(stream, filledView, done);
        }
      }
      function ReadableByteStreamControllerConvertPullIntoDescriptor(pullIntoDescriptor) {
        const bytesFilled = pullIntoDescriptor.bytesFilled;
        const elementSize = pullIntoDescriptor.elementSize;
        return new pullIntoDescriptor.viewConstructor(pullIntoDescriptor.buffer, pullIntoDescriptor.byteOffset, bytesFilled / elementSize);
      }
      function ReadableByteStreamControllerEnqueueChunkToQueue(controller, buffer, byteOffset, byteLength) {
        controller._queue.push({ buffer, byteOffset, byteLength });
        controller._queueTotalSize += byteLength;
      }
      function ReadableByteStreamControllerEnqueueClonedChunkToQueue(controller, buffer, byteOffset, byteLength) {
        let clonedChunk;
        try {
          clonedChunk = ArrayBufferSlice(buffer, byteOffset, byteOffset + byteLength);
        } catch (cloneE) {
          ReadableByteStreamControllerError(controller, cloneE);
          throw cloneE;
        }
        ReadableByteStreamControllerEnqueueChunkToQueue(controller, clonedChunk, 0, byteLength);
      }
      function ReadableByteStreamControllerEnqueueDetachedPullIntoToQueue(controller, firstDescriptor) {
        if (firstDescriptor.bytesFilled > 0) {
          ReadableByteStreamControllerEnqueueClonedChunkToQueue(controller, firstDescriptor.buffer, firstDescriptor.byteOffset, firstDescriptor.bytesFilled);
        }
        ReadableByteStreamControllerShiftPendingPullInto(controller);
      }
      function ReadableByteStreamControllerFillPullIntoDescriptorFromQueue(controller, pullIntoDescriptor) {
        const maxBytesToCopy = Math.min(controller._queueTotalSize, pullIntoDescriptor.byteLength - pullIntoDescriptor.bytesFilled);
        const maxBytesFilled = pullIntoDescriptor.bytesFilled + maxBytesToCopy;
        let totalBytesToCopyRemaining = maxBytesToCopy;
        let ready = false;
        const remainderBytes = maxBytesFilled % pullIntoDescriptor.elementSize;
        const maxAlignedBytes = maxBytesFilled - remainderBytes;
        if (maxAlignedBytes >= pullIntoDescriptor.minimumFill) {
          totalBytesToCopyRemaining = maxAlignedBytes - pullIntoDescriptor.bytesFilled;
          ready = true;
        }
        const queue = controller._queue;
        while (totalBytesToCopyRemaining > 0) {
          const headOfQueue = queue.peek();
          const bytesToCopy = Math.min(totalBytesToCopyRemaining, headOfQueue.byteLength);
          const destStart = pullIntoDescriptor.byteOffset + pullIntoDescriptor.bytesFilled;
          CopyDataBlockBytes(pullIntoDescriptor.buffer, destStart, headOfQueue.buffer, headOfQueue.byteOffset, bytesToCopy);
          if (headOfQueue.byteLength === bytesToCopy) {
            queue.shift();
          } else {
            headOfQueue.byteOffset += bytesToCopy;
            headOfQueue.byteLength -= bytesToCopy;
          }
          controller._queueTotalSize -= bytesToCopy;
          ReadableByteStreamControllerFillHeadPullIntoDescriptor(controller, bytesToCopy, pullIntoDescriptor);
          totalBytesToCopyRemaining -= bytesToCopy;
        }
        return ready;
      }
      function ReadableByteStreamControllerFillHeadPullIntoDescriptor(controller, size, pullIntoDescriptor) {
        pullIntoDescriptor.bytesFilled += size;
      }
      function ReadableByteStreamControllerHandleQueueDrain(controller) {
        if (controller._queueTotalSize === 0 && controller._closeRequested) {
          ReadableByteStreamControllerClearAlgorithms(controller);
          ReadableStreamClose(controller._controlledReadableByteStream);
        } else {
          ReadableByteStreamControllerCallPullIfNeeded(controller);
        }
      }
      function ReadableByteStreamControllerInvalidateBYOBRequest(controller) {
        if (controller._byobRequest === null) {
          return;
        }
        controller._byobRequest._associatedReadableByteStreamController = void 0;
        controller._byobRequest._view = null;
        controller._byobRequest = null;
      }
      function ReadableByteStreamControllerProcessPullIntoDescriptorsUsingQueue(controller) {
        while (controller._pendingPullIntos.length > 0) {
          if (controller._queueTotalSize === 0) {
            return;
          }
          const pullIntoDescriptor = controller._pendingPullIntos.peek();
          if (ReadableByteStreamControllerFillPullIntoDescriptorFromQueue(controller, pullIntoDescriptor)) {
            ReadableByteStreamControllerShiftPendingPullInto(controller);
            ReadableByteStreamControllerCommitPullIntoDescriptor(controller._controlledReadableByteStream, pullIntoDescriptor);
          }
        }
      }
      function ReadableByteStreamControllerProcessReadRequestsUsingQueue(controller) {
        const reader = controller._controlledReadableByteStream._reader;
        while (reader._readRequests.length > 0) {
          if (controller._queueTotalSize === 0) {
            return;
          }
          const readRequest = reader._readRequests.shift();
          ReadableByteStreamControllerFillReadRequestFromQueue(controller, readRequest);
        }
      }
      function ReadableByteStreamControllerPullInto(controller, view, min, readIntoRequest) {
        const stream = controller._controlledReadableByteStream;
        const ctor = view.constructor;
        const elementSize = arrayBufferViewElementSize(ctor);
        const { byteOffset, byteLength } = view;
        const minimumFill = min * elementSize;
        let buffer;
        try {
          buffer = TransferArrayBuffer(view.buffer);
        } catch (e2) {
          readIntoRequest._errorSteps(e2);
          return;
        }
        const pullIntoDescriptor = {
          buffer,
          bufferByteLength: buffer.byteLength,
          byteOffset,
          byteLength,
          bytesFilled: 0,
          minimumFill,
          elementSize,
          viewConstructor: ctor,
          readerType: "byob"
        };
        if (controller._pendingPullIntos.length > 0) {
          controller._pendingPullIntos.push(pullIntoDescriptor);
          ReadableStreamAddReadIntoRequest(stream, readIntoRequest);
          return;
        }
        if (stream._state === "closed") {
          const emptyView = new ctor(pullIntoDescriptor.buffer, pullIntoDescriptor.byteOffset, 0);
          readIntoRequest._closeSteps(emptyView);
          return;
        }
        if (controller._queueTotalSize > 0) {
          if (ReadableByteStreamControllerFillPullIntoDescriptorFromQueue(controller, pullIntoDescriptor)) {
            const filledView = ReadableByteStreamControllerConvertPullIntoDescriptor(pullIntoDescriptor);
            ReadableByteStreamControllerHandleQueueDrain(controller);
            readIntoRequest._chunkSteps(filledView);
            return;
          }
          if (controller._closeRequested) {
            const e2 = new TypeError("Insufficient bytes to fill elements in the given buffer");
            ReadableByteStreamControllerError(controller, e2);
            readIntoRequest._errorSteps(e2);
            return;
          }
        }
        controller._pendingPullIntos.push(pullIntoDescriptor);
        ReadableStreamAddReadIntoRequest(stream, readIntoRequest);
        ReadableByteStreamControllerCallPullIfNeeded(controller);
      }
      function ReadableByteStreamControllerRespondInClosedState(controller, firstDescriptor) {
        if (firstDescriptor.readerType === "none") {
          ReadableByteStreamControllerShiftPendingPullInto(controller);
        }
        const stream = controller._controlledReadableByteStream;
        if (ReadableStreamHasBYOBReader(stream)) {
          while (ReadableStreamGetNumReadIntoRequests(stream) > 0) {
            const pullIntoDescriptor = ReadableByteStreamControllerShiftPendingPullInto(controller);
            ReadableByteStreamControllerCommitPullIntoDescriptor(stream, pullIntoDescriptor);
          }
        }
      }
      function ReadableByteStreamControllerRespondInReadableState(controller, bytesWritten, pullIntoDescriptor) {
        ReadableByteStreamControllerFillHeadPullIntoDescriptor(controller, bytesWritten, pullIntoDescriptor);
        if (pullIntoDescriptor.readerType === "none") {
          ReadableByteStreamControllerEnqueueDetachedPullIntoToQueue(controller, pullIntoDescriptor);
          ReadableByteStreamControllerProcessPullIntoDescriptorsUsingQueue(controller);
          return;
        }
        if (pullIntoDescriptor.bytesFilled < pullIntoDescriptor.minimumFill) {
          return;
        }
        ReadableByteStreamControllerShiftPendingPullInto(controller);
        const remainderSize = pullIntoDescriptor.bytesFilled % pullIntoDescriptor.elementSize;
        if (remainderSize > 0) {
          const end = pullIntoDescriptor.byteOffset + pullIntoDescriptor.bytesFilled;
          ReadableByteStreamControllerEnqueueClonedChunkToQueue(controller, pullIntoDescriptor.buffer, end - remainderSize, remainderSize);
        }
        pullIntoDescriptor.bytesFilled -= remainderSize;
        ReadableByteStreamControllerCommitPullIntoDescriptor(controller._controlledReadableByteStream, pullIntoDescriptor);
        ReadableByteStreamControllerProcessPullIntoDescriptorsUsingQueue(controller);
      }
      function ReadableByteStreamControllerRespondInternal(controller, bytesWritten) {
        const firstDescriptor = controller._pendingPullIntos.peek();
        ReadableByteStreamControllerInvalidateBYOBRequest(controller);
        const state = controller._controlledReadableByteStream._state;
        if (state === "closed") {
          ReadableByteStreamControllerRespondInClosedState(controller, firstDescriptor);
        } else {
          ReadableByteStreamControllerRespondInReadableState(controller, bytesWritten, firstDescriptor);
        }
        ReadableByteStreamControllerCallPullIfNeeded(controller);
      }
      function ReadableByteStreamControllerShiftPendingPullInto(controller) {
        const descriptor = controller._pendingPullIntos.shift();
        return descriptor;
      }
      function ReadableByteStreamControllerShouldCallPull(controller) {
        const stream = controller._controlledReadableByteStream;
        if (stream._state !== "readable") {
          return false;
        }
        if (controller._closeRequested) {
          return false;
        }
        if (!controller._started) {
          return false;
        }
        if (ReadableStreamHasDefaultReader(stream) && ReadableStreamGetNumReadRequests(stream) > 0) {
          return true;
        }
        if (ReadableStreamHasBYOBReader(stream) && ReadableStreamGetNumReadIntoRequests(stream) > 0) {
          return true;
        }
        const desiredSize = ReadableByteStreamControllerGetDesiredSize(controller);
        if (desiredSize > 0) {
          return true;
        }
        return false;
      }
      function ReadableByteStreamControllerClearAlgorithms(controller) {
        controller._pullAlgorithm = void 0;
        controller._cancelAlgorithm = void 0;
      }
      function ReadableByteStreamControllerClose(controller) {
        const stream = controller._controlledReadableByteStream;
        if (controller._closeRequested || stream._state !== "readable") {
          return;
        }
        if (controller._queueTotalSize > 0) {
          controller._closeRequested = true;
          return;
        }
        if (controller._pendingPullIntos.length > 0) {
          const firstPendingPullInto = controller._pendingPullIntos.peek();
          if (firstPendingPullInto.bytesFilled % firstPendingPullInto.elementSize !== 0) {
            const e2 = new TypeError("Insufficient bytes to fill elements in the given buffer");
            ReadableByteStreamControllerError(controller, e2);
            throw e2;
          }
        }
        ReadableByteStreamControllerClearAlgorithms(controller);
        ReadableStreamClose(stream);
      }
      function ReadableByteStreamControllerEnqueue(controller, chunk) {
        const stream = controller._controlledReadableByteStream;
        if (controller._closeRequested || stream._state !== "readable") {
          return;
        }
        const { buffer, byteOffset, byteLength } = chunk;
        if (IsDetachedBuffer(buffer)) {
          throw new TypeError("chunk's buffer is detached and so cannot be enqueued");
        }
        const transferredBuffer = TransferArrayBuffer(buffer);
        if (controller._pendingPullIntos.length > 0) {
          const firstPendingPullInto = controller._pendingPullIntos.peek();
          if (IsDetachedBuffer(firstPendingPullInto.buffer)) {
            throw new TypeError("The BYOB request's buffer has been detached and so cannot be filled with an enqueued chunk");
          }
          ReadableByteStreamControllerInvalidateBYOBRequest(controller);
          firstPendingPullInto.buffer = TransferArrayBuffer(firstPendingPullInto.buffer);
          if (firstPendingPullInto.readerType === "none") {
            ReadableByteStreamControllerEnqueueDetachedPullIntoToQueue(controller, firstPendingPullInto);
          }
        }
        if (ReadableStreamHasDefaultReader(stream)) {
          ReadableByteStreamControllerProcessReadRequestsUsingQueue(controller);
          if (ReadableStreamGetNumReadRequests(stream) === 0) {
            ReadableByteStreamControllerEnqueueChunkToQueue(controller, transferredBuffer, byteOffset, byteLength);
          } else {
            if (controller._pendingPullIntos.length > 0) {
              ReadableByteStreamControllerShiftPendingPullInto(controller);
            }
            const transferredView = new Uint8Array(transferredBuffer, byteOffset, byteLength);
            ReadableStreamFulfillReadRequest(stream, transferredView, false);
          }
        } else if (ReadableStreamHasBYOBReader(stream)) {
          ReadableByteStreamControllerEnqueueChunkToQueue(controller, transferredBuffer, byteOffset, byteLength);
          ReadableByteStreamControllerProcessPullIntoDescriptorsUsingQueue(controller);
        } else {
          ReadableByteStreamControllerEnqueueChunkToQueue(controller, transferredBuffer, byteOffset, byteLength);
        }
        ReadableByteStreamControllerCallPullIfNeeded(controller);
      }
      function ReadableByteStreamControllerError(controller, e2) {
        const stream = controller._controlledReadableByteStream;
        if (stream._state !== "readable") {
          return;
        }
        ReadableByteStreamControllerClearPendingPullIntos(controller);
        ResetQueue(controller);
        ReadableByteStreamControllerClearAlgorithms(controller);
        ReadableStreamError(stream, e2);
      }
      function ReadableByteStreamControllerFillReadRequestFromQueue(controller, readRequest) {
        const entry = controller._queue.shift();
        controller._queueTotalSize -= entry.byteLength;
        ReadableByteStreamControllerHandleQueueDrain(controller);
        const view = new Uint8Array(entry.buffer, entry.byteOffset, entry.byteLength);
        readRequest._chunkSteps(view);
      }
      function ReadableByteStreamControllerGetBYOBRequest(controller) {
        if (controller._byobRequest === null && controller._pendingPullIntos.length > 0) {
          const firstDescriptor = controller._pendingPullIntos.peek();
          const view = new Uint8Array(firstDescriptor.buffer, firstDescriptor.byteOffset + firstDescriptor.bytesFilled, firstDescriptor.byteLength - firstDescriptor.bytesFilled);
          const byobRequest = Object.create(ReadableStreamBYOBRequest.prototype);
          SetUpReadableStreamBYOBRequest(byobRequest, controller, view);
          controller._byobRequest = byobRequest;
        }
        return controller._byobRequest;
      }
      function ReadableByteStreamControllerGetDesiredSize(controller) {
        const state = controller._controlledReadableByteStream._state;
        if (state === "errored") {
          return null;
        }
        if (state === "closed") {
          return 0;
        }
        return controller._strategyHWM - controller._queueTotalSize;
      }
      function ReadableByteStreamControllerRespond(controller, bytesWritten) {
        const firstDescriptor = controller._pendingPullIntos.peek();
        const state = controller._controlledReadableByteStream._state;
        if (state === "closed") {
          if (bytesWritten !== 0) {
            throw new TypeError("bytesWritten must be 0 when calling respond() on a closed stream");
          }
        } else {
          if (bytesWritten === 0) {
            throw new TypeError("bytesWritten must be greater than 0 when calling respond() on a readable stream");
          }
          if (firstDescriptor.bytesFilled + bytesWritten > firstDescriptor.byteLength) {
            throw new RangeError("bytesWritten out of range");
          }
        }
        firstDescriptor.buffer = TransferArrayBuffer(firstDescriptor.buffer);
        ReadableByteStreamControllerRespondInternal(controller, bytesWritten);
      }
      function ReadableByteStreamControllerRespondWithNewView(controller, view) {
        const firstDescriptor = controller._pendingPullIntos.peek();
        const state = controller._controlledReadableByteStream._state;
        if (state === "closed") {
          if (view.byteLength !== 0) {
            throw new TypeError("The view's length must be 0 when calling respondWithNewView() on a closed stream");
          }
        } else {
          if (view.byteLength === 0) {
            throw new TypeError("The view's length must be greater than 0 when calling respondWithNewView() on a readable stream");
          }
        }
        if (firstDescriptor.byteOffset + firstDescriptor.bytesFilled !== view.byteOffset) {
          throw new RangeError("The region specified by view does not match byobRequest");
        }
        if (firstDescriptor.bufferByteLength !== view.buffer.byteLength) {
          throw new RangeError("The buffer of view has different capacity than byobRequest");
        }
        if (firstDescriptor.bytesFilled + view.byteLength > firstDescriptor.byteLength) {
          throw new RangeError("The region specified by view is larger than byobRequest");
        }
        const viewByteLength = view.byteLength;
        firstDescriptor.buffer = TransferArrayBuffer(view.buffer);
        ReadableByteStreamControllerRespondInternal(controller, viewByteLength);
      }
      function SetUpReadableByteStreamController(stream, controller, startAlgorithm, pullAlgorithm, cancelAlgorithm, highWaterMark, autoAllocateChunkSize) {
        controller._controlledReadableByteStream = stream;
        controller._pullAgain = false;
        controller._pulling = false;
        controller._byobRequest = null;
        controller._queue = controller._queueTotalSize = void 0;
        ResetQueue(controller);
        controller._closeRequested = false;
        controller._started = false;
        controller._strategyHWM = highWaterMark;
        controller._pullAlgorithm = pullAlgorithm;
        controller._cancelAlgorithm = cancelAlgorithm;
        controller._autoAllocateChunkSize = autoAllocateChunkSize;
        controller._pendingPullIntos = new SimpleQueue();
        stream._readableStreamController = controller;
        const startResult = startAlgorithm();
        uponPromise(promiseResolvedWith(startResult), () => {
          controller._started = true;
          ReadableByteStreamControllerCallPullIfNeeded(controller);
          return null;
        }, (r2) => {
          ReadableByteStreamControllerError(controller, r2);
          return null;
        });
      }
      function SetUpReadableByteStreamControllerFromUnderlyingSource(stream, underlyingByteSource, highWaterMark) {
        const controller = Object.create(ReadableByteStreamController.prototype);
        let startAlgorithm;
        let pullAlgorithm;
        let cancelAlgorithm;
        if (underlyingByteSource.start !== void 0) {
          startAlgorithm = () => underlyingByteSource.start(controller);
        } else {
          startAlgorithm = () => void 0;
        }
        if (underlyingByteSource.pull !== void 0) {
          pullAlgorithm = () => underlyingByteSource.pull(controller);
        } else {
          pullAlgorithm = () => promiseResolvedWith(void 0);
        }
        if (underlyingByteSource.cancel !== void 0) {
          cancelAlgorithm = (reason) => underlyingByteSource.cancel(reason);
        } else {
          cancelAlgorithm = () => promiseResolvedWith(void 0);
        }
        const autoAllocateChunkSize = underlyingByteSource.autoAllocateChunkSize;
        if (autoAllocateChunkSize === 0) {
          throw new TypeError("autoAllocateChunkSize must be greater than 0");
        }
        SetUpReadableByteStreamController(stream, controller, startAlgorithm, pullAlgorithm, cancelAlgorithm, highWaterMark, autoAllocateChunkSize);
      }
      function SetUpReadableStreamBYOBRequest(request, controller, view) {
        request._associatedReadableByteStreamController = controller;
        request._view = view;
      }
      function byobRequestBrandCheckException(name) {
        return new TypeError(`ReadableStreamBYOBRequest.prototype.${name} can only be used on a ReadableStreamBYOBRequest`);
      }
      function byteStreamControllerBrandCheckException(name) {
        return new TypeError(`ReadableByteStreamController.prototype.${name} can only be used on a ReadableByteStreamController`);
      }
      function convertReaderOptions(options, context) {
        assertDictionary(options, context);
        const mode = options === null || options === void 0 ? void 0 : options.mode;
        return {
          mode: mode === void 0 ? void 0 : convertReadableStreamReaderMode(mode, `${context} has member 'mode' that`)
        };
      }
      function convertReadableStreamReaderMode(mode, context) {
        mode = `${mode}`;
        if (mode !== "byob") {
          throw new TypeError(`${context} '${mode}' is not a valid enumeration value for ReadableStreamReaderMode`);
        }
        return mode;
      }
      function convertByobReadOptions(options, context) {
        var _a2;
        assertDictionary(options, context);
        const min = (_a2 = options === null || options === void 0 ? void 0 : options.min) !== null && _a2 !== void 0 ? _a2 : 1;
        return {
          min: convertUnsignedLongLongWithEnforceRange(min, `${context} has member 'min' that`)
        };
      }
      function AcquireReadableStreamBYOBReader(stream) {
        return new ReadableStreamBYOBReader(stream);
      }
      function ReadableStreamAddReadIntoRequest(stream, readIntoRequest) {
        stream._reader._readIntoRequests.push(readIntoRequest);
      }
      function ReadableStreamFulfillReadIntoRequest(stream, chunk, done) {
        const reader = stream._reader;
        const readIntoRequest = reader._readIntoRequests.shift();
        if (done) {
          readIntoRequest._closeSteps(chunk);
        } else {
          readIntoRequest._chunkSteps(chunk);
        }
      }
      function ReadableStreamGetNumReadIntoRequests(stream) {
        return stream._reader._readIntoRequests.length;
      }
      function ReadableStreamHasBYOBReader(stream) {
        const reader = stream._reader;
        if (reader === void 0) {
          return false;
        }
        if (!IsReadableStreamBYOBReader(reader)) {
          return false;
        }
        return true;
      }
      class ReadableStreamBYOBReader {
        constructor(stream) {
          assertRequiredArgument(stream, 1, "ReadableStreamBYOBReader");
          assertReadableStream(stream, "First parameter");
          if (IsReadableStreamLocked(stream)) {
            throw new TypeError("This stream has already been locked for exclusive reading by another reader");
          }
          if (!IsReadableByteStreamController(stream._readableStreamController)) {
            throw new TypeError("Cannot construct a ReadableStreamBYOBReader for a stream not constructed with a byte source");
          }
          ReadableStreamReaderGenericInitialize(this, stream);
          this._readIntoRequests = new SimpleQueue();
        }
        /**
         * Returns a promise that will be fulfilled when the stream becomes closed, or rejected if the stream ever errors or
         * the reader's lock is released before the stream finishes closing.
         */
        get closed() {
          if (!IsReadableStreamBYOBReader(this)) {
            return promiseRejectedWith(byobReaderBrandCheckException("closed"));
          }
          return this._closedPromise;
        }
        /**
         * If the reader is active, behaves the same as {@link ReadableStream.cancel | stream.cancel(reason)}.
         */
        cancel(reason = void 0) {
          if (!IsReadableStreamBYOBReader(this)) {
            return promiseRejectedWith(byobReaderBrandCheckException("cancel"));
          }
          if (this._ownerReadableStream === void 0) {
            return promiseRejectedWith(readerLockException("cancel"));
          }
          return ReadableStreamReaderGenericCancel(this, reason);
        }
        read(view, rawOptions = {}) {
          if (!IsReadableStreamBYOBReader(this)) {
            return promiseRejectedWith(byobReaderBrandCheckException("read"));
          }
          if (!ArrayBuffer.isView(view)) {
            return promiseRejectedWith(new TypeError("view must be an array buffer view"));
          }
          if (view.byteLength === 0) {
            return promiseRejectedWith(new TypeError("view must have non-zero byteLength"));
          }
          if (view.buffer.byteLength === 0) {
            return promiseRejectedWith(new TypeError(`view's buffer must have non-zero byteLength`));
          }
          if (IsDetachedBuffer(view.buffer)) {
            return promiseRejectedWith(new TypeError("view's buffer has been detached"));
          }
          let options;
          try {
            options = convertByobReadOptions(rawOptions, "options");
          } catch (e2) {
            return promiseRejectedWith(e2);
          }
          const min = options.min;
          if (min === 0) {
            return promiseRejectedWith(new TypeError("options.min must be greater than 0"));
          }
          if (!isDataView(view)) {
            if (min > view.length) {
              return promiseRejectedWith(new RangeError("options.min must be less than or equal to view's length"));
            }
          } else if (min > view.byteLength) {
            return promiseRejectedWith(new RangeError("options.min must be less than or equal to view's byteLength"));
          }
          if (this._ownerReadableStream === void 0) {
            return promiseRejectedWith(readerLockException("read from"));
          }
          let resolvePromise;
          let rejectPromise;
          const promise = newPromise((resolve, reject) => {
            resolvePromise = resolve;
            rejectPromise = reject;
          });
          const readIntoRequest = {
            _chunkSteps: (chunk) => resolvePromise({ value: chunk, done: false }),
            _closeSteps: (chunk) => resolvePromise({ value: chunk, done: true }),
            _errorSteps: (e2) => rejectPromise(e2)
          };
          ReadableStreamBYOBReaderRead(this, view, min, readIntoRequest);
          return promise;
        }
        /**
         * Releases the reader's lock on the corresponding stream. After the lock is released, the reader is no longer active.
         * If the associated stream is errored when the lock is released, the reader will appear errored in the same way
         * from now on; otherwise, the reader will appear closed.
         *
         * A reader's lock cannot be released while it still has a pending read request, i.e., if a promise returned by
         * the reader's {@link ReadableStreamBYOBReader.read | read()} method has not yet been settled. Attempting to
         * do so will throw a `TypeError` and leave the reader locked to the stream.
         */
        releaseLock() {
          if (!IsReadableStreamBYOBReader(this)) {
            throw byobReaderBrandCheckException("releaseLock");
          }
          if (this._ownerReadableStream === void 0) {
            return;
          }
          ReadableStreamBYOBReaderRelease(this);
        }
      }
      Object.defineProperties(ReadableStreamBYOBReader.prototype, {
        cancel: { enumerable: true },
        read: { enumerable: true },
        releaseLock: { enumerable: true },
        closed: { enumerable: true }
      });
      setFunctionName(ReadableStreamBYOBReader.prototype.cancel, "cancel");
      setFunctionName(ReadableStreamBYOBReader.prototype.read, "read");
      setFunctionName(ReadableStreamBYOBReader.prototype.releaseLock, "releaseLock");
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(ReadableStreamBYOBReader.prototype, Symbol.toStringTag, {
          value: "ReadableStreamBYOBReader",
          configurable: true
        });
      }
      function IsReadableStreamBYOBReader(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_readIntoRequests")) {
          return false;
        }
        return x2 instanceof ReadableStreamBYOBReader;
      }
      function ReadableStreamBYOBReaderRead(reader, view, min, readIntoRequest) {
        const stream = reader._ownerReadableStream;
        stream._disturbed = true;
        if (stream._state === "errored") {
          readIntoRequest._errorSteps(stream._storedError);
        } else {
          ReadableByteStreamControllerPullInto(stream._readableStreamController, view, min, readIntoRequest);
        }
      }
      function ReadableStreamBYOBReaderRelease(reader) {
        ReadableStreamReaderGenericRelease(reader);
        const e2 = new TypeError("Reader was released");
        ReadableStreamBYOBReaderErrorReadIntoRequests(reader, e2);
      }
      function ReadableStreamBYOBReaderErrorReadIntoRequests(reader, e2) {
        const readIntoRequests = reader._readIntoRequests;
        reader._readIntoRequests = new SimpleQueue();
        readIntoRequests.forEach((readIntoRequest) => {
          readIntoRequest._errorSteps(e2);
        });
      }
      function byobReaderBrandCheckException(name) {
        return new TypeError(`ReadableStreamBYOBReader.prototype.${name} can only be used on a ReadableStreamBYOBReader`);
      }
      function ExtractHighWaterMark(strategy, defaultHWM) {
        const { highWaterMark } = strategy;
        if (highWaterMark === void 0) {
          return defaultHWM;
        }
        if (NumberIsNaN(highWaterMark) || highWaterMark < 0) {
          throw new RangeError("Invalid highWaterMark");
        }
        return highWaterMark;
      }
      function ExtractSizeAlgorithm(strategy) {
        const { size } = strategy;
        if (!size) {
          return () => 1;
        }
        return size;
      }
      function convertQueuingStrategy(init, context) {
        assertDictionary(init, context);
        const highWaterMark = init === null || init === void 0 ? void 0 : init.highWaterMark;
        const size = init === null || init === void 0 ? void 0 : init.size;
        return {
          highWaterMark: highWaterMark === void 0 ? void 0 : convertUnrestrictedDouble(highWaterMark),
          size: size === void 0 ? void 0 : convertQueuingStrategySize(size, `${context} has member 'size' that`)
        };
      }
      function convertQueuingStrategySize(fn, context) {
        assertFunction(fn, context);
        return (chunk) => convertUnrestrictedDouble(fn(chunk));
      }
      function convertUnderlyingSink(original, context) {
        assertDictionary(original, context);
        const abort = original === null || original === void 0 ? void 0 : original.abort;
        const close = original === null || original === void 0 ? void 0 : original.close;
        const start = original === null || original === void 0 ? void 0 : original.start;
        const type = original === null || original === void 0 ? void 0 : original.type;
        const write = original === null || original === void 0 ? void 0 : original.write;
        return {
          abort: abort === void 0 ? void 0 : convertUnderlyingSinkAbortCallback(abort, original, `${context} has member 'abort' that`),
          close: close === void 0 ? void 0 : convertUnderlyingSinkCloseCallback(close, original, `${context} has member 'close' that`),
          start: start === void 0 ? void 0 : convertUnderlyingSinkStartCallback(start, original, `${context} has member 'start' that`),
          write: write === void 0 ? void 0 : convertUnderlyingSinkWriteCallback(write, original, `${context} has member 'write' that`),
          type
        };
      }
      function convertUnderlyingSinkAbortCallback(fn, original, context) {
        assertFunction(fn, context);
        return (reason) => promiseCall(fn, original, [reason]);
      }
      function convertUnderlyingSinkCloseCallback(fn, original, context) {
        assertFunction(fn, context);
        return () => promiseCall(fn, original, []);
      }
      function convertUnderlyingSinkStartCallback(fn, original, context) {
        assertFunction(fn, context);
        return (controller) => reflectCall(fn, original, [controller]);
      }
      function convertUnderlyingSinkWriteCallback(fn, original, context) {
        assertFunction(fn, context);
        return (chunk, controller) => promiseCall(fn, original, [chunk, controller]);
      }
      function assertWritableStream(x2, context) {
        if (!IsWritableStream(x2)) {
          throw new TypeError(`${context} is not a WritableStream.`);
        }
      }
      function isAbortSignal2(value) {
        if (typeof value !== "object" || value === null) {
          return false;
        }
        try {
          return typeof value.aborted === "boolean";
        } catch (_a2) {
          return false;
        }
      }
      const supportsAbortController = typeof AbortController === "function";
      function createAbortController() {
        if (supportsAbortController) {
          return new AbortController();
        }
        return void 0;
      }
      class WritableStream {
        constructor(rawUnderlyingSink = {}, rawStrategy = {}) {
          if (rawUnderlyingSink === void 0) {
            rawUnderlyingSink = null;
          } else {
            assertObject(rawUnderlyingSink, "First parameter");
          }
          const strategy = convertQueuingStrategy(rawStrategy, "Second parameter");
          const underlyingSink = convertUnderlyingSink(rawUnderlyingSink, "First parameter");
          InitializeWritableStream(this);
          const type = underlyingSink.type;
          if (type !== void 0) {
            throw new RangeError("Invalid type is specified");
          }
          const sizeAlgorithm = ExtractSizeAlgorithm(strategy);
          const highWaterMark = ExtractHighWaterMark(strategy, 1);
          SetUpWritableStreamDefaultControllerFromUnderlyingSink(this, underlyingSink, highWaterMark, sizeAlgorithm);
        }
        /**
         * Returns whether or not the writable stream is locked to a writer.
         */
        get locked() {
          if (!IsWritableStream(this)) {
            throw streamBrandCheckException$2("locked");
          }
          return IsWritableStreamLocked(this);
        }
        /**
         * Aborts the stream, signaling that the producer can no longer successfully write to the stream and it is to be
         * immediately moved to an errored state, with any queued-up writes discarded. This will also execute any abort
         * mechanism of the underlying sink.
         *
         * The returned promise will fulfill if the stream shuts down successfully, or reject if the underlying sink signaled
         * that there was an error doing so. Additionally, it will reject with a `TypeError` (without attempting to cancel
         * the stream) if the stream is currently locked.
         */
        abort(reason = void 0) {
          if (!IsWritableStream(this)) {
            return promiseRejectedWith(streamBrandCheckException$2("abort"));
          }
          if (IsWritableStreamLocked(this)) {
            return promiseRejectedWith(new TypeError("Cannot abort a stream that already has a writer"));
          }
          return WritableStreamAbort(this, reason);
        }
        /**
         * Closes the stream. The underlying sink will finish processing any previously-written chunks, before invoking its
         * close behavior. During this time any further attempts to write will fail (without erroring the stream).
         *
         * The method returns a promise that will fulfill if all remaining chunks are successfully written and the stream
         * successfully closes, or rejects if an error is encountered during this process. Additionally, it will reject with
         * a `TypeError` (without attempting to cancel the stream) if the stream is currently locked.
         */
        close() {
          if (!IsWritableStream(this)) {
            return promiseRejectedWith(streamBrandCheckException$2("close"));
          }
          if (IsWritableStreamLocked(this)) {
            return promiseRejectedWith(new TypeError("Cannot close a stream that already has a writer"));
          }
          if (WritableStreamCloseQueuedOrInFlight(this)) {
            return promiseRejectedWith(new TypeError("Cannot close an already-closing stream"));
          }
          return WritableStreamClose(this);
        }
        /**
         * Creates a {@link WritableStreamDefaultWriter | writer} and locks the stream to the new writer. While the stream
         * is locked, no other writer can be acquired until this one is released.
         *
         * This functionality is especially useful for creating abstractions that desire the ability to write to a stream
         * without interruption or interleaving. By getting a writer for the stream, you can ensure nobody else can write at
         * the same time, which would cause the resulting written data to be unpredictable and probably useless.
         */
        getWriter() {
          if (!IsWritableStream(this)) {
            throw streamBrandCheckException$2("getWriter");
          }
          return AcquireWritableStreamDefaultWriter(this);
        }
      }
      Object.defineProperties(WritableStream.prototype, {
        abort: { enumerable: true },
        close: { enumerable: true },
        getWriter: { enumerable: true },
        locked: { enumerable: true }
      });
      setFunctionName(WritableStream.prototype.abort, "abort");
      setFunctionName(WritableStream.prototype.close, "close");
      setFunctionName(WritableStream.prototype.getWriter, "getWriter");
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(WritableStream.prototype, Symbol.toStringTag, {
          value: "WritableStream",
          configurable: true
        });
      }
      function AcquireWritableStreamDefaultWriter(stream) {
        return new WritableStreamDefaultWriter(stream);
      }
      function CreateWritableStream(startAlgorithm, writeAlgorithm, closeAlgorithm, abortAlgorithm, highWaterMark = 1, sizeAlgorithm = () => 1) {
        const stream = Object.create(WritableStream.prototype);
        InitializeWritableStream(stream);
        const controller = Object.create(WritableStreamDefaultController.prototype);
        SetUpWritableStreamDefaultController(stream, controller, startAlgorithm, writeAlgorithm, closeAlgorithm, abortAlgorithm, highWaterMark, sizeAlgorithm);
        return stream;
      }
      function InitializeWritableStream(stream) {
        stream._state = "writable";
        stream._storedError = void 0;
        stream._writer = void 0;
        stream._writableStreamController = void 0;
        stream._writeRequests = new SimpleQueue();
        stream._inFlightWriteRequest = void 0;
        stream._closeRequest = void 0;
        stream._inFlightCloseRequest = void 0;
        stream._pendingAbortRequest = void 0;
        stream._backpressure = false;
      }
      function IsWritableStream(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_writableStreamController")) {
          return false;
        }
        return x2 instanceof WritableStream;
      }
      function IsWritableStreamLocked(stream) {
        if (stream._writer === void 0) {
          return false;
        }
        return true;
      }
      function WritableStreamAbort(stream, reason) {
        var _a2;
        if (stream._state === "closed" || stream._state === "errored") {
          return promiseResolvedWith(void 0);
        }
        stream._writableStreamController._abortReason = reason;
        (_a2 = stream._writableStreamController._abortController) === null || _a2 === void 0 ? void 0 : _a2.abort(reason);
        const state = stream._state;
        if (state === "closed" || state === "errored") {
          return promiseResolvedWith(void 0);
        }
        if (stream._pendingAbortRequest !== void 0) {
          return stream._pendingAbortRequest._promise;
        }
        let wasAlreadyErroring = false;
        if (state === "erroring") {
          wasAlreadyErroring = true;
          reason = void 0;
        }
        const promise = newPromise((resolve, reject) => {
          stream._pendingAbortRequest = {
            _promise: void 0,
            _resolve: resolve,
            _reject: reject,
            _reason: reason,
            _wasAlreadyErroring: wasAlreadyErroring
          };
        });
        stream._pendingAbortRequest._promise = promise;
        if (!wasAlreadyErroring) {
          WritableStreamStartErroring(stream, reason);
        }
        return promise;
      }
      function WritableStreamClose(stream) {
        const state = stream._state;
        if (state === "closed" || state === "errored") {
          return promiseRejectedWith(new TypeError(`The stream (in ${state} state) is not in the writable state and cannot be closed`));
        }
        const promise = newPromise((resolve, reject) => {
          const closeRequest = {
            _resolve: resolve,
            _reject: reject
          };
          stream._closeRequest = closeRequest;
        });
        const writer = stream._writer;
        if (writer !== void 0 && stream._backpressure && state === "writable") {
          defaultWriterReadyPromiseResolve(writer);
        }
        WritableStreamDefaultControllerClose(stream._writableStreamController);
        return promise;
      }
      function WritableStreamAddWriteRequest(stream) {
        const promise = newPromise((resolve, reject) => {
          const writeRequest = {
            _resolve: resolve,
            _reject: reject
          };
          stream._writeRequests.push(writeRequest);
        });
        return promise;
      }
      function WritableStreamDealWithRejection(stream, error) {
        const state = stream._state;
        if (state === "writable") {
          WritableStreamStartErroring(stream, error);
          return;
        }
        WritableStreamFinishErroring(stream);
      }
      function WritableStreamStartErroring(stream, reason) {
        const controller = stream._writableStreamController;
        stream._state = "erroring";
        stream._storedError = reason;
        const writer = stream._writer;
        if (writer !== void 0) {
          WritableStreamDefaultWriterEnsureReadyPromiseRejected(writer, reason);
        }
        if (!WritableStreamHasOperationMarkedInFlight(stream) && controller._started) {
          WritableStreamFinishErroring(stream);
        }
      }
      function WritableStreamFinishErroring(stream) {
        stream._state = "errored";
        stream._writableStreamController[ErrorSteps]();
        const storedError = stream._storedError;
        stream._writeRequests.forEach((writeRequest) => {
          writeRequest._reject(storedError);
        });
        stream._writeRequests = new SimpleQueue();
        if (stream._pendingAbortRequest === void 0) {
          WritableStreamRejectCloseAndClosedPromiseIfNeeded(stream);
          return;
        }
        const abortRequest = stream._pendingAbortRequest;
        stream._pendingAbortRequest = void 0;
        if (abortRequest._wasAlreadyErroring) {
          abortRequest._reject(storedError);
          WritableStreamRejectCloseAndClosedPromiseIfNeeded(stream);
          return;
        }
        const promise = stream._writableStreamController[AbortSteps](abortRequest._reason);
        uponPromise(promise, () => {
          abortRequest._resolve();
          WritableStreamRejectCloseAndClosedPromiseIfNeeded(stream);
          return null;
        }, (reason) => {
          abortRequest._reject(reason);
          WritableStreamRejectCloseAndClosedPromiseIfNeeded(stream);
          return null;
        });
      }
      function WritableStreamFinishInFlightWrite(stream) {
        stream._inFlightWriteRequest._resolve(void 0);
        stream._inFlightWriteRequest = void 0;
      }
      function WritableStreamFinishInFlightWriteWithError(stream, error) {
        stream._inFlightWriteRequest._reject(error);
        stream._inFlightWriteRequest = void 0;
        WritableStreamDealWithRejection(stream, error);
      }
      function WritableStreamFinishInFlightClose(stream) {
        stream._inFlightCloseRequest._resolve(void 0);
        stream._inFlightCloseRequest = void 0;
        const state = stream._state;
        if (state === "erroring") {
          stream._storedError = void 0;
          if (stream._pendingAbortRequest !== void 0) {
            stream._pendingAbortRequest._resolve();
            stream._pendingAbortRequest = void 0;
          }
        }
        stream._state = "closed";
        const writer = stream._writer;
        if (writer !== void 0) {
          defaultWriterClosedPromiseResolve(writer);
        }
      }
      function WritableStreamFinishInFlightCloseWithError(stream, error) {
        stream._inFlightCloseRequest._reject(error);
        stream._inFlightCloseRequest = void 0;
        if (stream._pendingAbortRequest !== void 0) {
          stream._pendingAbortRequest._reject(error);
          stream._pendingAbortRequest = void 0;
        }
        WritableStreamDealWithRejection(stream, error);
      }
      function WritableStreamCloseQueuedOrInFlight(stream) {
        if (stream._closeRequest === void 0 && stream._inFlightCloseRequest === void 0) {
          return false;
        }
        return true;
      }
      function WritableStreamHasOperationMarkedInFlight(stream) {
        if (stream._inFlightWriteRequest === void 0 && stream._inFlightCloseRequest === void 0) {
          return false;
        }
        return true;
      }
      function WritableStreamMarkCloseRequestInFlight(stream) {
        stream._inFlightCloseRequest = stream._closeRequest;
        stream._closeRequest = void 0;
      }
      function WritableStreamMarkFirstWriteRequestInFlight(stream) {
        stream._inFlightWriteRequest = stream._writeRequests.shift();
      }
      function WritableStreamRejectCloseAndClosedPromiseIfNeeded(stream) {
        if (stream._closeRequest !== void 0) {
          stream._closeRequest._reject(stream._storedError);
          stream._closeRequest = void 0;
        }
        const writer = stream._writer;
        if (writer !== void 0) {
          defaultWriterClosedPromiseReject(writer, stream._storedError);
        }
      }
      function WritableStreamUpdateBackpressure(stream, backpressure) {
        const writer = stream._writer;
        if (writer !== void 0 && backpressure !== stream._backpressure) {
          if (backpressure) {
            defaultWriterReadyPromiseReset(writer);
          } else {
            defaultWriterReadyPromiseResolve(writer);
          }
        }
        stream._backpressure = backpressure;
      }
      class WritableStreamDefaultWriter {
        constructor(stream) {
          assertRequiredArgument(stream, 1, "WritableStreamDefaultWriter");
          assertWritableStream(stream, "First parameter");
          if (IsWritableStreamLocked(stream)) {
            throw new TypeError("This stream has already been locked for exclusive writing by another writer");
          }
          this._ownerWritableStream = stream;
          stream._writer = this;
          const state = stream._state;
          if (state === "writable") {
            if (!WritableStreamCloseQueuedOrInFlight(stream) && stream._backpressure) {
              defaultWriterReadyPromiseInitialize(this);
            } else {
              defaultWriterReadyPromiseInitializeAsResolved(this);
            }
            defaultWriterClosedPromiseInitialize(this);
          } else if (state === "erroring") {
            defaultWriterReadyPromiseInitializeAsRejected(this, stream._storedError);
            defaultWriterClosedPromiseInitialize(this);
          } else if (state === "closed") {
            defaultWriterReadyPromiseInitializeAsResolved(this);
            defaultWriterClosedPromiseInitializeAsResolved(this);
          } else {
            const storedError = stream._storedError;
            defaultWriterReadyPromiseInitializeAsRejected(this, storedError);
            defaultWriterClosedPromiseInitializeAsRejected(this, storedError);
          }
        }
        /**
         * Returns a promise that will be fulfilled when the stream becomes closed, or rejected if the stream ever errors or
         * the writer’s lock is released before the stream finishes closing.
         */
        get closed() {
          if (!IsWritableStreamDefaultWriter(this)) {
            return promiseRejectedWith(defaultWriterBrandCheckException("closed"));
          }
          return this._closedPromise;
        }
        /**
         * Returns the desired size to fill the stream’s internal queue. It can be negative, if the queue is over-full.
         * A producer can use this information to determine the right amount of data to write.
         *
         * It will be `null` if the stream cannot be successfully written to (due to either being errored, or having an abort
         * queued up). It will return zero if the stream is closed. And the getter will throw an exception if invoked when
         * the writer’s lock is released.
         */
        get desiredSize() {
          if (!IsWritableStreamDefaultWriter(this)) {
            throw defaultWriterBrandCheckException("desiredSize");
          }
          if (this._ownerWritableStream === void 0) {
            throw defaultWriterLockException("desiredSize");
          }
          return WritableStreamDefaultWriterGetDesiredSize(this);
        }
        /**
         * Returns a promise that will be fulfilled when the desired size to fill the stream’s internal queue transitions
         * from non-positive to positive, signaling that it is no longer applying backpressure. Once the desired size dips
         * back to zero or below, the getter will return a new promise that stays pending until the next transition.
         *
         * If the stream becomes errored or aborted, or the writer’s lock is released, the returned promise will become
         * rejected.
         */
        get ready() {
          if (!IsWritableStreamDefaultWriter(this)) {
            return promiseRejectedWith(defaultWriterBrandCheckException("ready"));
          }
          return this._readyPromise;
        }
        /**
         * If the reader is active, behaves the same as {@link WritableStream.abort | stream.abort(reason)}.
         */
        abort(reason = void 0) {
          if (!IsWritableStreamDefaultWriter(this)) {
            return promiseRejectedWith(defaultWriterBrandCheckException("abort"));
          }
          if (this._ownerWritableStream === void 0) {
            return promiseRejectedWith(defaultWriterLockException("abort"));
          }
          return WritableStreamDefaultWriterAbort(this, reason);
        }
        /**
         * If the reader is active, behaves the same as {@link WritableStream.close | stream.close()}.
         */
        close() {
          if (!IsWritableStreamDefaultWriter(this)) {
            return promiseRejectedWith(defaultWriterBrandCheckException("close"));
          }
          const stream = this._ownerWritableStream;
          if (stream === void 0) {
            return promiseRejectedWith(defaultWriterLockException("close"));
          }
          if (WritableStreamCloseQueuedOrInFlight(stream)) {
            return promiseRejectedWith(new TypeError("Cannot close an already-closing stream"));
          }
          return WritableStreamDefaultWriterClose(this);
        }
        /**
         * Releases the writer’s lock on the corresponding stream. After the lock is released, the writer is no longer active.
         * If the associated stream is errored when the lock is released, the writer will appear errored in the same way from
         * now on; otherwise, the writer will appear closed.
         *
         * Note that the lock can still be released even if some ongoing writes have not yet finished (i.e. even if the
         * promises returned from previous calls to {@link WritableStreamDefaultWriter.write | write()} have not yet settled).
         * It’s not necessary to hold the lock on the writer for the duration of the write; the lock instead simply prevents
         * other producers from writing in an interleaved manner.
         */
        releaseLock() {
          if (!IsWritableStreamDefaultWriter(this)) {
            throw defaultWriterBrandCheckException("releaseLock");
          }
          const stream = this._ownerWritableStream;
          if (stream === void 0) {
            return;
          }
          WritableStreamDefaultWriterRelease(this);
        }
        write(chunk = void 0) {
          if (!IsWritableStreamDefaultWriter(this)) {
            return promiseRejectedWith(defaultWriterBrandCheckException("write"));
          }
          if (this._ownerWritableStream === void 0) {
            return promiseRejectedWith(defaultWriterLockException("write to"));
          }
          return WritableStreamDefaultWriterWrite(this, chunk);
        }
      }
      Object.defineProperties(WritableStreamDefaultWriter.prototype, {
        abort: { enumerable: true },
        close: { enumerable: true },
        releaseLock: { enumerable: true },
        write: { enumerable: true },
        closed: { enumerable: true },
        desiredSize: { enumerable: true },
        ready: { enumerable: true }
      });
      setFunctionName(WritableStreamDefaultWriter.prototype.abort, "abort");
      setFunctionName(WritableStreamDefaultWriter.prototype.close, "close");
      setFunctionName(WritableStreamDefaultWriter.prototype.releaseLock, "releaseLock");
      setFunctionName(WritableStreamDefaultWriter.prototype.write, "write");
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(WritableStreamDefaultWriter.prototype, Symbol.toStringTag, {
          value: "WritableStreamDefaultWriter",
          configurable: true
        });
      }
      function IsWritableStreamDefaultWriter(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_ownerWritableStream")) {
          return false;
        }
        return x2 instanceof WritableStreamDefaultWriter;
      }
      function WritableStreamDefaultWriterAbort(writer, reason) {
        const stream = writer._ownerWritableStream;
        return WritableStreamAbort(stream, reason);
      }
      function WritableStreamDefaultWriterClose(writer) {
        const stream = writer._ownerWritableStream;
        return WritableStreamClose(stream);
      }
      function WritableStreamDefaultWriterCloseWithErrorPropagation(writer) {
        const stream = writer._ownerWritableStream;
        const state = stream._state;
        if (WritableStreamCloseQueuedOrInFlight(stream) || state === "closed") {
          return promiseResolvedWith(void 0);
        }
        if (state === "errored") {
          return promiseRejectedWith(stream._storedError);
        }
        return WritableStreamDefaultWriterClose(writer);
      }
      function WritableStreamDefaultWriterEnsureClosedPromiseRejected(writer, error) {
        if (writer._closedPromiseState === "pending") {
          defaultWriterClosedPromiseReject(writer, error);
        } else {
          defaultWriterClosedPromiseResetToRejected(writer, error);
        }
      }
      function WritableStreamDefaultWriterEnsureReadyPromiseRejected(writer, error) {
        if (writer._readyPromiseState === "pending") {
          defaultWriterReadyPromiseReject(writer, error);
        } else {
          defaultWriterReadyPromiseResetToRejected(writer, error);
        }
      }
      function WritableStreamDefaultWriterGetDesiredSize(writer) {
        const stream = writer._ownerWritableStream;
        const state = stream._state;
        if (state === "errored" || state === "erroring") {
          return null;
        }
        if (state === "closed") {
          return 0;
        }
        return WritableStreamDefaultControllerGetDesiredSize(stream._writableStreamController);
      }
      function WritableStreamDefaultWriterRelease(writer) {
        const stream = writer._ownerWritableStream;
        const releasedError = new TypeError(`Writer was released and can no longer be used to monitor the stream's closedness`);
        WritableStreamDefaultWriterEnsureReadyPromiseRejected(writer, releasedError);
        WritableStreamDefaultWriterEnsureClosedPromiseRejected(writer, releasedError);
        stream._writer = void 0;
        writer._ownerWritableStream = void 0;
      }
      function WritableStreamDefaultWriterWrite(writer, chunk) {
        const stream = writer._ownerWritableStream;
        const controller = stream._writableStreamController;
        const chunkSize = WritableStreamDefaultControllerGetChunkSize(controller, chunk);
        if (stream !== writer._ownerWritableStream) {
          return promiseRejectedWith(defaultWriterLockException("write to"));
        }
        const state = stream._state;
        if (state === "errored") {
          return promiseRejectedWith(stream._storedError);
        }
        if (WritableStreamCloseQueuedOrInFlight(stream) || state === "closed") {
          return promiseRejectedWith(new TypeError("The stream is closing or closed and cannot be written to"));
        }
        if (state === "erroring") {
          return promiseRejectedWith(stream._storedError);
        }
        const promise = WritableStreamAddWriteRequest(stream);
        WritableStreamDefaultControllerWrite(controller, chunk, chunkSize);
        return promise;
      }
      const closeSentinel = {};
      class WritableStreamDefaultController {
        constructor() {
          throw new TypeError("Illegal constructor");
        }
        /**
         * The reason which was passed to `WritableStream.abort(reason)` when the stream was aborted.
         *
         * @deprecated
         *  This property has been removed from the specification, see https://github.com/whatwg/streams/pull/1177.
         *  Use {@link WritableStreamDefaultController.signal}'s `reason` instead.
         */
        get abortReason() {
          if (!IsWritableStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException$2("abortReason");
          }
          return this._abortReason;
        }
        /**
         * An `AbortSignal` that can be used to abort the pending write or close operation when the stream is aborted.
         */
        get signal() {
          if (!IsWritableStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException$2("signal");
          }
          if (this._abortController === void 0) {
            throw new TypeError("WritableStreamDefaultController.prototype.signal is not supported");
          }
          return this._abortController.signal;
        }
        /**
         * Closes the controlled writable stream, making all future interactions with it fail with the given error `e`.
         *
         * This method is rarely used, since usually it suffices to return a rejected promise from one of the underlying
         * sink's methods. However, it can be useful for suddenly shutting down a stream in response to an event outside the
         * normal lifecycle of interactions with the underlying sink.
         */
        error(e2 = void 0) {
          if (!IsWritableStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException$2("error");
          }
          const state = this._controlledWritableStream._state;
          if (state !== "writable") {
            return;
          }
          WritableStreamDefaultControllerError(this, e2);
        }
        /** @internal */
        [AbortSteps](reason) {
          const result = this._abortAlgorithm(reason);
          WritableStreamDefaultControllerClearAlgorithms(this);
          return result;
        }
        /** @internal */
        [ErrorSteps]() {
          ResetQueue(this);
        }
      }
      Object.defineProperties(WritableStreamDefaultController.prototype, {
        abortReason: { enumerable: true },
        signal: { enumerable: true },
        error: { enumerable: true }
      });
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(WritableStreamDefaultController.prototype, Symbol.toStringTag, {
          value: "WritableStreamDefaultController",
          configurable: true
        });
      }
      function IsWritableStreamDefaultController(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_controlledWritableStream")) {
          return false;
        }
        return x2 instanceof WritableStreamDefaultController;
      }
      function SetUpWritableStreamDefaultController(stream, controller, startAlgorithm, writeAlgorithm, closeAlgorithm, abortAlgorithm, highWaterMark, sizeAlgorithm) {
        controller._controlledWritableStream = stream;
        stream._writableStreamController = controller;
        controller._queue = void 0;
        controller._queueTotalSize = void 0;
        ResetQueue(controller);
        controller._abortReason = void 0;
        controller._abortController = createAbortController();
        controller._started = false;
        controller._strategySizeAlgorithm = sizeAlgorithm;
        controller._strategyHWM = highWaterMark;
        controller._writeAlgorithm = writeAlgorithm;
        controller._closeAlgorithm = closeAlgorithm;
        controller._abortAlgorithm = abortAlgorithm;
        const backpressure = WritableStreamDefaultControllerGetBackpressure(controller);
        WritableStreamUpdateBackpressure(stream, backpressure);
        const startResult = startAlgorithm();
        const startPromise = promiseResolvedWith(startResult);
        uponPromise(startPromise, () => {
          controller._started = true;
          WritableStreamDefaultControllerAdvanceQueueIfNeeded(controller);
          return null;
        }, (r2) => {
          controller._started = true;
          WritableStreamDealWithRejection(stream, r2);
          return null;
        });
      }
      function SetUpWritableStreamDefaultControllerFromUnderlyingSink(stream, underlyingSink, highWaterMark, sizeAlgorithm) {
        const controller = Object.create(WritableStreamDefaultController.prototype);
        let startAlgorithm;
        let writeAlgorithm;
        let closeAlgorithm;
        let abortAlgorithm;
        if (underlyingSink.start !== void 0) {
          startAlgorithm = () => underlyingSink.start(controller);
        } else {
          startAlgorithm = () => void 0;
        }
        if (underlyingSink.write !== void 0) {
          writeAlgorithm = (chunk) => underlyingSink.write(chunk, controller);
        } else {
          writeAlgorithm = () => promiseResolvedWith(void 0);
        }
        if (underlyingSink.close !== void 0) {
          closeAlgorithm = () => underlyingSink.close();
        } else {
          closeAlgorithm = () => promiseResolvedWith(void 0);
        }
        if (underlyingSink.abort !== void 0) {
          abortAlgorithm = (reason) => underlyingSink.abort(reason);
        } else {
          abortAlgorithm = () => promiseResolvedWith(void 0);
        }
        SetUpWritableStreamDefaultController(stream, controller, startAlgorithm, writeAlgorithm, closeAlgorithm, abortAlgorithm, highWaterMark, sizeAlgorithm);
      }
      function WritableStreamDefaultControllerClearAlgorithms(controller) {
        controller._writeAlgorithm = void 0;
        controller._closeAlgorithm = void 0;
        controller._abortAlgorithm = void 0;
        controller._strategySizeAlgorithm = void 0;
      }
      function WritableStreamDefaultControllerClose(controller) {
        EnqueueValueWithSize(controller, closeSentinel, 0);
        WritableStreamDefaultControllerAdvanceQueueIfNeeded(controller);
      }
      function WritableStreamDefaultControllerGetChunkSize(controller, chunk) {
        try {
          return controller._strategySizeAlgorithm(chunk);
        } catch (chunkSizeE) {
          WritableStreamDefaultControllerErrorIfNeeded(controller, chunkSizeE);
          return 1;
        }
      }
      function WritableStreamDefaultControllerGetDesiredSize(controller) {
        return controller._strategyHWM - controller._queueTotalSize;
      }
      function WritableStreamDefaultControllerWrite(controller, chunk, chunkSize) {
        try {
          EnqueueValueWithSize(controller, chunk, chunkSize);
        } catch (enqueueE) {
          WritableStreamDefaultControllerErrorIfNeeded(controller, enqueueE);
          return;
        }
        const stream = controller._controlledWritableStream;
        if (!WritableStreamCloseQueuedOrInFlight(stream) && stream._state === "writable") {
          const backpressure = WritableStreamDefaultControllerGetBackpressure(controller);
          WritableStreamUpdateBackpressure(stream, backpressure);
        }
        WritableStreamDefaultControllerAdvanceQueueIfNeeded(controller);
      }
      function WritableStreamDefaultControllerAdvanceQueueIfNeeded(controller) {
        const stream = controller._controlledWritableStream;
        if (!controller._started) {
          return;
        }
        if (stream._inFlightWriteRequest !== void 0) {
          return;
        }
        const state = stream._state;
        if (state === "erroring") {
          WritableStreamFinishErroring(stream);
          return;
        }
        if (controller._queue.length === 0) {
          return;
        }
        const value = PeekQueueValue(controller);
        if (value === closeSentinel) {
          WritableStreamDefaultControllerProcessClose(controller);
        } else {
          WritableStreamDefaultControllerProcessWrite(controller, value);
        }
      }
      function WritableStreamDefaultControllerErrorIfNeeded(controller, error) {
        if (controller._controlledWritableStream._state === "writable") {
          WritableStreamDefaultControllerError(controller, error);
        }
      }
      function WritableStreamDefaultControllerProcessClose(controller) {
        const stream = controller._controlledWritableStream;
        WritableStreamMarkCloseRequestInFlight(stream);
        DequeueValue(controller);
        const sinkClosePromise = controller._closeAlgorithm();
        WritableStreamDefaultControllerClearAlgorithms(controller);
        uponPromise(sinkClosePromise, () => {
          WritableStreamFinishInFlightClose(stream);
          return null;
        }, (reason) => {
          WritableStreamFinishInFlightCloseWithError(stream, reason);
          return null;
        });
      }
      function WritableStreamDefaultControllerProcessWrite(controller, chunk) {
        const stream = controller._controlledWritableStream;
        WritableStreamMarkFirstWriteRequestInFlight(stream);
        const sinkWritePromise = controller._writeAlgorithm(chunk);
        uponPromise(sinkWritePromise, () => {
          WritableStreamFinishInFlightWrite(stream);
          const state = stream._state;
          DequeueValue(controller);
          if (!WritableStreamCloseQueuedOrInFlight(stream) && state === "writable") {
            const backpressure = WritableStreamDefaultControllerGetBackpressure(controller);
            WritableStreamUpdateBackpressure(stream, backpressure);
          }
          WritableStreamDefaultControllerAdvanceQueueIfNeeded(controller);
          return null;
        }, (reason) => {
          if (stream._state === "writable") {
            WritableStreamDefaultControllerClearAlgorithms(controller);
          }
          WritableStreamFinishInFlightWriteWithError(stream, reason);
          return null;
        });
      }
      function WritableStreamDefaultControllerGetBackpressure(controller) {
        const desiredSize = WritableStreamDefaultControllerGetDesiredSize(controller);
        return desiredSize <= 0;
      }
      function WritableStreamDefaultControllerError(controller, error) {
        const stream = controller._controlledWritableStream;
        WritableStreamDefaultControllerClearAlgorithms(controller);
        WritableStreamStartErroring(stream, error);
      }
      function streamBrandCheckException$2(name) {
        return new TypeError(`WritableStream.prototype.${name} can only be used on a WritableStream`);
      }
      function defaultControllerBrandCheckException$2(name) {
        return new TypeError(`WritableStreamDefaultController.prototype.${name} can only be used on a WritableStreamDefaultController`);
      }
      function defaultWriterBrandCheckException(name) {
        return new TypeError(`WritableStreamDefaultWriter.prototype.${name} can only be used on a WritableStreamDefaultWriter`);
      }
      function defaultWriterLockException(name) {
        return new TypeError("Cannot " + name + " a stream using a released writer");
      }
      function defaultWriterClosedPromiseInitialize(writer) {
        writer._closedPromise = newPromise((resolve, reject) => {
          writer._closedPromise_resolve = resolve;
          writer._closedPromise_reject = reject;
          writer._closedPromiseState = "pending";
        });
      }
      function defaultWriterClosedPromiseInitializeAsRejected(writer, reason) {
        defaultWriterClosedPromiseInitialize(writer);
        defaultWriterClosedPromiseReject(writer, reason);
      }
      function defaultWriterClosedPromiseInitializeAsResolved(writer) {
        defaultWriterClosedPromiseInitialize(writer);
        defaultWriterClosedPromiseResolve(writer);
      }
      function defaultWriterClosedPromiseReject(writer, reason) {
        if (writer._closedPromise_reject === void 0) {
          return;
        }
        setPromiseIsHandledToTrue(writer._closedPromise);
        writer._closedPromise_reject(reason);
        writer._closedPromise_resolve = void 0;
        writer._closedPromise_reject = void 0;
        writer._closedPromiseState = "rejected";
      }
      function defaultWriterClosedPromiseResetToRejected(writer, reason) {
        defaultWriterClosedPromiseInitializeAsRejected(writer, reason);
      }
      function defaultWriterClosedPromiseResolve(writer) {
        if (writer._closedPromise_resolve === void 0) {
          return;
        }
        writer._closedPromise_resolve(void 0);
        writer._closedPromise_resolve = void 0;
        writer._closedPromise_reject = void 0;
        writer._closedPromiseState = "resolved";
      }
      function defaultWriterReadyPromiseInitialize(writer) {
        writer._readyPromise = newPromise((resolve, reject) => {
          writer._readyPromise_resolve = resolve;
          writer._readyPromise_reject = reject;
        });
        writer._readyPromiseState = "pending";
      }
      function defaultWriterReadyPromiseInitializeAsRejected(writer, reason) {
        defaultWriterReadyPromiseInitialize(writer);
        defaultWriterReadyPromiseReject(writer, reason);
      }
      function defaultWriterReadyPromiseInitializeAsResolved(writer) {
        defaultWriterReadyPromiseInitialize(writer);
        defaultWriterReadyPromiseResolve(writer);
      }
      function defaultWriterReadyPromiseReject(writer, reason) {
        if (writer._readyPromise_reject === void 0) {
          return;
        }
        setPromiseIsHandledToTrue(writer._readyPromise);
        writer._readyPromise_reject(reason);
        writer._readyPromise_resolve = void 0;
        writer._readyPromise_reject = void 0;
        writer._readyPromiseState = "rejected";
      }
      function defaultWriterReadyPromiseReset(writer) {
        defaultWriterReadyPromiseInitialize(writer);
      }
      function defaultWriterReadyPromiseResetToRejected(writer, reason) {
        defaultWriterReadyPromiseInitializeAsRejected(writer, reason);
      }
      function defaultWriterReadyPromiseResolve(writer) {
        if (writer._readyPromise_resolve === void 0) {
          return;
        }
        writer._readyPromise_resolve(void 0);
        writer._readyPromise_resolve = void 0;
        writer._readyPromise_reject = void 0;
        writer._readyPromiseState = "fulfilled";
      }
      function getGlobals() {
        if (typeof globalThis !== "undefined") {
          return globalThis;
        } else if (typeof self !== "undefined") {
          return self;
        } else if (typeof global !== "undefined") {
          return global;
        }
        return void 0;
      }
      const globals = getGlobals();
      function isDOMExceptionConstructor(ctor) {
        if (!(typeof ctor === "function" || typeof ctor === "object")) {
          return false;
        }
        if (ctor.name !== "DOMException") {
          return false;
        }
        try {
          new ctor();
          return true;
        } catch (_a2) {
          return false;
        }
      }
      function getFromGlobal() {
        const ctor = globals === null || globals === void 0 ? void 0 : globals.DOMException;
        return isDOMExceptionConstructor(ctor) ? ctor : void 0;
      }
      function createPolyfill() {
        const ctor = function DOMException3(message, name) {
          this.message = message || "";
          this.name = name || "Error";
          if (Error.captureStackTrace) {
            Error.captureStackTrace(this, this.constructor);
          }
        };
        setFunctionName(ctor, "DOMException");
        ctor.prototype = Object.create(Error.prototype);
        Object.defineProperty(ctor.prototype, "constructor", { value: ctor, writable: true, configurable: true });
        return ctor;
      }
      const DOMException2 = getFromGlobal() || createPolyfill();
      function ReadableStreamPipeTo(source, dest, preventClose, preventAbort, preventCancel, signal) {
        const reader = AcquireReadableStreamDefaultReader(source);
        const writer = AcquireWritableStreamDefaultWriter(dest);
        source._disturbed = true;
        let shuttingDown = false;
        let currentWrite = promiseResolvedWith(void 0);
        return newPromise((resolve, reject) => {
          let abortAlgorithm;
          if (signal !== void 0) {
            abortAlgorithm = () => {
              const error = signal.reason !== void 0 ? signal.reason : new DOMException2("Aborted", "AbortError");
              const actions = [];
              if (!preventAbort) {
                actions.push(() => {
                  if (dest._state === "writable") {
                    return WritableStreamAbort(dest, error);
                  }
                  return promiseResolvedWith(void 0);
                });
              }
              if (!preventCancel) {
                actions.push(() => {
                  if (source._state === "readable") {
                    return ReadableStreamCancel(source, error);
                  }
                  return promiseResolvedWith(void 0);
                });
              }
              shutdownWithAction(() => Promise.all(actions.map((action) => action())), true, error);
            };
            if (signal.aborted) {
              abortAlgorithm();
              return;
            }
            signal.addEventListener("abort", abortAlgorithm);
          }
          function pipeLoop() {
            return newPromise((resolveLoop, rejectLoop) => {
              function next(done) {
                if (done) {
                  resolveLoop();
                } else {
                  PerformPromiseThen(pipeStep(), next, rejectLoop);
                }
              }
              next(false);
            });
          }
          function pipeStep() {
            if (shuttingDown) {
              return promiseResolvedWith(true);
            }
            return PerformPromiseThen(writer._readyPromise, () => {
              return newPromise((resolveRead, rejectRead) => {
                ReadableStreamDefaultReaderRead(reader, {
                  _chunkSteps: (chunk) => {
                    currentWrite = PerformPromiseThen(WritableStreamDefaultWriterWrite(writer, chunk), void 0, noop2);
                    resolveRead(false);
                  },
                  _closeSteps: () => resolveRead(true),
                  _errorSteps: rejectRead
                });
              });
            });
          }
          isOrBecomesErrored(source, reader._closedPromise, (storedError) => {
            if (!preventAbort) {
              shutdownWithAction(() => WritableStreamAbort(dest, storedError), true, storedError);
            } else {
              shutdown(true, storedError);
            }
            return null;
          });
          isOrBecomesErrored(dest, writer._closedPromise, (storedError) => {
            if (!preventCancel) {
              shutdownWithAction(() => ReadableStreamCancel(source, storedError), true, storedError);
            } else {
              shutdown(true, storedError);
            }
            return null;
          });
          isOrBecomesClosed(source, reader._closedPromise, () => {
            if (!preventClose) {
              shutdownWithAction(() => WritableStreamDefaultWriterCloseWithErrorPropagation(writer));
            } else {
              shutdown();
            }
            return null;
          });
          if (WritableStreamCloseQueuedOrInFlight(dest) || dest._state === "closed") {
            const destClosed = new TypeError("the destination writable stream closed before all data could be piped to it");
            if (!preventCancel) {
              shutdownWithAction(() => ReadableStreamCancel(source, destClosed), true, destClosed);
            } else {
              shutdown(true, destClosed);
            }
          }
          setPromiseIsHandledToTrue(pipeLoop());
          function waitForWritesToFinish() {
            const oldCurrentWrite = currentWrite;
            return PerformPromiseThen(currentWrite, () => oldCurrentWrite !== currentWrite ? waitForWritesToFinish() : void 0);
          }
          function isOrBecomesErrored(stream, promise, action) {
            if (stream._state === "errored") {
              action(stream._storedError);
            } else {
              uponRejection(promise, action);
            }
          }
          function isOrBecomesClosed(stream, promise, action) {
            if (stream._state === "closed") {
              action();
            } else {
              uponFulfillment(promise, action);
            }
          }
          function shutdownWithAction(action, originalIsError, originalError) {
            if (shuttingDown) {
              return;
            }
            shuttingDown = true;
            if (dest._state === "writable" && !WritableStreamCloseQueuedOrInFlight(dest)) {
              uponFulfillment(waitForWritesToFinish(), doTheRest);
            } else {
              doTheRest();
            }
            function doTheRest() {
              uponPromise(action(), () => finalize(originalIsError, originalError), (newError) => finalize(true, newError));
              return null;
            }
          }
          function shutdown(isError, error) {
            if (shuttingDown) {
              return;
            }
            shuttingDown = true;
            if (dest._state === "writable" && !WritableStreamCloseQueuedOrInFlight(dest)) {
              uponFulfillment(waitForWritesToFinish(), () => finalize(isError, error));
            } else {
              finalize(isError, error);
            }
          }
          function finalize(isError, error) {
            WritableStreamDefaultWriterRelease(writer);
            ReadableStreamReaderGenericRelease(reader);
            if (signal !== void 0) {
              signal.removeEventListener("abort", abortAlgorithm);
            }
            if (isError) {
              reject(error);
            } else {
              resolve(void 0);
            }
            return null;
          }
        });
      }
      class ReadableStreamDefaultController {
        constructor() {
          throw new TypeError("Illegal constructor");
        }
        /**
         * Returns the desired size to fill the controlled stream's internal queue. It can be negative, if the queue is
         * over-full. An underlying source ought to use this information to determine when and how to apply backpressure.
         */
        get desiredSize() {
          if (!IsReadableStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException$1("desiredSize");
          }
          return ReadableStreamDefaultControllerGetDesiredSize(this);
        }
        /**
         * Closes the controlled readable stream. Consumers will still be able to read any previously-enqueued chunks from
         * the stream, but once those are read, the stream will become closed.
         */
        close() {
          if (!IsReadableStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException$1("close");
          }
          if (!ReadableStreamDefaultControllerCanCloseOrEnqueue(this)) {
            throw new TypeError("The stream is not in a state that permits close");
          }
          ReadableStreamDefaultControllerClose(this);
        }
        enqueue(chunk = void 0) {
          if (!IsReadableStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException$1("enqueue");
          }
          if (!ReadableStreamDefaultControllerCanCloseOrEnqueue(this)) {
            throw new TypeError("The stream is not in a state that permits enqueue");
          }
          return ReadableStreamDefaultControllerEnqueue(this, chunk);
        }
        /**
         * Errors the controlled readable stream, making all future interactions with it fail with the given error `e`.
         */
        error(e2 = void 0) {
          if (!IsReadableStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException$1("error");
          }
          ReadableStreamDefaultControllerError(this, e2);
        }
        /** @internal */
        [CancelSteps](reason) {
          ResetQueue(this);
          const result = this._cancelAlgorithm(reason);
          ReadableStreamDefaultControllerClearAlgorithms(this);
          return result;
        }
        /** @internal */
        [PullSteps](readRequest) {
          const stream = this._controlledReadableStream;
          if (this._queue.length > 0) {
            const chunk = DequeueValue(this);
            if (this._closeRequested && this._queue.length === 0) {
              ReadableStreamDefaultControllerClearAlgorithms(this);
              ReadableStreamClose(stream);
            } else {
              ReadableStreamDefaultControllerCallPullIfNeeded(this);
            }
            readRequest._chunkSteps(chunk);
          } else {
            ReadableStreamAddReadRequest(stream, readRequest);
            ReadableStreamDefaultControllerCallPullIfNeeded(this);
          }
        }
        /** @internal */
        [ReleaseSteps]() {
        }
      }
      Object.defineProperties(ReadableStreamDefaultController.prototype, {
        close: { enumerable: true },
        enqueue: { enumerable: true },
        error: { enumerable: true },
        desiredSize: { enumerable: true }
      });
      setFunctionName(ReadableStreamDefaultController.prototype.close, "close");
      setFunctionName(ReadableStreamDefaultController.prototype.enqueue, "enqueue");
      setFunctionName(ReadableStreamDefaultController.prototype.error, "error");
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(ReadableStreamDefaultController.prototype, Symbol.toStringTag, {
          value: "ReadableStreamDefaultController",
          configurable: true
        });
      }
      function IsReadableStreamDefaultController(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_controlledReadableStream")) {
          return false;
        }
        return x2 instanceof ReadableStreamDefaultController;
      }
      function ReadableStreamDefaultControllerCallPullIfNeeded(controller) {
        const shouldPull = ReadableStreamDefaultControllerShouldCallPull(controller);
        if (!shouldPull) {
          return;
        }
        if (controller._pulling) {
          controller._pullAgain = true;
          return;
        }
        controller._pulling = true;
        const pullPromise = controller._pullAlgorithm();
        uponPromise(pullPromise, () => {
          controller._pulling = false;
          if (controller._pullAgain) {
            controller._pullAgain = false;
            ReadableStreamDefaultControllerCallPullIfNeeded(controller);
          }
          return null;
        }, (e2) => {
          ReadableStreamDefaultControllerError(controller, e2);
          return null;
        });
      }
      function ReadableStreamDefaultControllerShouldCallPull(controller) {
        const stream = controller._controlledReadableStream;
        if (!ReadableStreamDefaultControllerCanCloseOrEnqueue(controller)) {
          return false;
        }
        if (!controller._started) {
          return false;
        }
        if (IsReadableStreamLocked(stream) && ReadableStreamGetNumReadRequests(stream) > 0) {
          return true;
        }
        const desiredSize = ReadableStreamDefaultControllerGetDesiredSize(controller);
        if (desiredSize > 0) {
          return true;
        }
        return false;
      }
      function ReadableStreamDefaultControllerClearAlgorithms(controller) {
        controller._pullAlgorithm = void 0;
        controller._cancelAlgorithm = void 0;
        controller._strategySizeAlgorithm = void 0;
      }
      function ReadableStreamDefaultControllerClose(controller) {
        if (!ReadableStreamDefaultControllerCanCloseOrEnqueue(controller)) {
          return;
        }
        const stream = controller._controlledReadableStream;
        controller._closeRequested = true;
        if (controller._queue.length === 0) {
          ReadableStreamDefaultControllerClearAlgorithms(controller);
          ReadableStreamClose(stream);
        }
      }
      function ReadableStreamDefaultControllerEnqueue(controller, chunk) {
        if (!ReadableStreamDefaultControllerCanCloseOrEnqueue(controller)) {
          return;
        }
        const stream = controller._controlledReadableStream;
        if (IsReadableStreamLocked(stream) && ReadableStreamGetNumReadRequests(stream) > 0) {
          ReadableStreamFulfillReadRequest(stream, chunk, false);
        } else {
          let chunkSize;
          try {
            chunkSize = controller._strategySizeAlgorithm(chunk);
          } catch (chunkSizeE) {
            ReadableStreamDefaultControllerError(controller, chunkSizeE);
            throw chunkSizeE;
          }
          try {
            EnqueueValueWithSize(controller, chunk, chunkSize);
          } catch (enqueueE) {
            ReadableStreamDefaultControllerError(controller, enqueueE);
            throw enqueueE;
          }
        }
        ReadableStreamDefaultControllerCallPullIfNeeded(controller);
      }
      function ReadableStreamDefaultControllerError(controller, e2) {
        const stream = controller._controlledReadableStream;
        if (stream._state !== "readable") {
          return;
        }
        ResetQueue(controller);
        ReadableStreamDefaultControllerClearAlgorithms(controller);
        ReadableStreamError(stream, e2);
      }
      function ReadableStreamDefaultControllerGetDesiredSize(controller) {
        const state = controller._controlledReadableStream._state;
        if (state === "errored") {
          return null;
        }
        if (state === "closed") {
          return 0;
        }
        return controller._strategyHWM - controller._queueTotalSize;
      }
      function ReadableStreamDefaultControllerHasBackpressure(controller) {
        if (ReadableStreamDefaultControllerShouldCallPull(controller)) {
          return false;
        }
        return true;
      }
      function ReadableStreamDefaultControllerCanCloseOrEnqueue(controller) {
        const state = controller._controlledReadableStream._state;
        if (!controller._closeRequested && state === "readable") {
          return true;
        }
        return false;
      }
      function SetUpReadableStreamDefaultController(stream, controller, startAlgorithm, pullAlgorithm, cancelAlgorithm, highWaterMark, sizeAlgorithm) {
        controller._controlledReadableStream = stream;
        controller._queue = void 0;
        controller._queueTotalSize = void 0;
        ResetQueue(controller);
        controller._started = false;
        controller._closeRequested = false;
        controller._pullAgain = false;
        controller._pulling = false;
        controller._strategySizeAlgorithm = sizeAlgorithm;
        controller._strategyHWM = highWaterMark;
        controller._pullAlgorithm = pullAlgorithm;
        controller._cancelAlgorithm = cancelAlgorithm;
        stream._readableStreamController = controller;
        const startResult = startAlgorithm();
        uponPromise(promiseResolvedWith(startResult), () => {
          controller._started = true;
          ReadableStreamDefaultControllerCallPullIfNeeded(controller);
          return null;
        }, (r2) => {
          ReadableStreamDefaultControllerError(controller, r2);
          return null;
        });
      }
      function SetUpReadableStreamDefaultControllerFromUnderlyingSource(stream, underlyingSource, highWaterMark, sizeAlgorithm) {
        const controller = Object.create(ReadableStreamDefaultController.prototype);
        let startAlgorithm;
        let pullAlgorithm;
        let cancelAlgorithm;
        if (underlyingSource.start !== void 0) {
          startAlgorithm = () => underlyingSource.start(controller);
        } else {
          startAlgorithm = () => void 0;
        }
        if (underlyingSource.pull !== void 0) {
          pullAlgorithm = () => underlyingSource.pull(controller);
        } else {
          pullAlgorithm = () => promiseResolvedWith(void 0);
        }
        if (underlyingSource.cancel !== void 0) {
          cancelAlgorithm = (reason) => underlyingSource.cancel(reason);
        } else {
          cancelAlgorithm = () => promiseResolvedWith(void 0);
        }
        SetUpReadableStreamDefaultController(stream, controller, startAlgorithm, pullAlgorithm, cancelAlgorithm, highWaterMark, sizeAlgorithm);
      }
      function defaultControllerBrandCheckException$1(name) {
        return new TypeError(`ReadableStreamDefaultController.prototype.${name} can only be used on a ReadableStreamDefaultController`);
      }
      function ReadableStreamTee(stream, cloneForBranch2) {
        if (IsReadableByteStreamController(stream._readableStreamController)) {
          return ReadableByteStreamTee(stream);
        }
        return ReadableStreamDefaultTee(stream);
      }
      function ReadableStreamDefaultTee(stream, cloneForBranch2) {
        const reader = AcquireReadableStreamDefaultReader(stream);
        let reading = false;
        let readAgain = false;
        let canceled1 = false;
        let canceled2 = false;
        let reason1;
        let reason2;
        let branch1;
        let branch2;
        let resolveCancelPromise;
        const cancelPromise = newPromise((resolve) => {
          resolveCancelPromise = resolve;
        });
        function pullAlgorithm() {
          if (reading) {
            readAgain = true;
            return promiseResolvedWith(void 0);
          }
          reading = true;
          const readRequest = {
            _chunkSteps: (chunk) => {
              _queueMicrotask(() => {
                readAgain = false;
                const chunk1 = chunk;
                const chunk2 = chunk;
                if (!canceled1) {
                  ReadableStreamDefaultControllerEnqueue(branch1._readableStreamController, chunk1);
                }
                if (!canceled2) {
                  ReadableStreamDefaultControllerEnqueue(branch2._readableStreamController, chunk2);
                }
                reading = false;
                if (readAgain) {
                  pullAlgorithm();
                }
              });
            },
            _closeSteps: () => {
              reading = false;
              if (!canceled1) {
                ReadableStreamDefaultControllerClose(branch1._readableStreamController);
              }
              if (!canceled2) {
                ReadableStreamDefaultControllerClose(branch2._readableStreamController);
              }
              if (!canceled1 || !canceled2) {
                resolveCancelPromise(void 0);
              }
            },
            _errorSteps: () => {
              reading = false;
            }
          };
          ReadableStreamDefaultReaderRead(reader, readRequest);
          return promiseResolvedWith(void 0);
        }
        function cancel1Algorithm(reason) {
          canceled1 = true;
          reason1 = reason;
          if (canceled2) {
            const compositeReason = CreateArrayFromList([reason1, reason2]);
            const cancelResult = ReadableStreamCancel(stream, compositeReason);
            resolveCancelPromise(cancelResult);
          }
          return cancelPromise;
        }
        function cancel2Algorithm(reason) {
          canceled2 = true;
          reason2 = reason;
          if (canceled1) {
            const compositeReason = CreateArrayFromList([reason1, reason2]);
            const cancelResult = ReadableStreamCancel(stream, compositeReason);
            resolveCancelPromise(cancelResult);
          }
          return cancelPromise;
        }
        function startAlgorithm() {
        }
        branch1 = CreateReadableStream(startAlgorithm, pullAlgorithm, cancel1Algorithm);
        branch2 = CreateReadableStream(startAlgorithm, pullAlgorithm, cancel2Algorithm);
        uponRejection(reader._closedPromise, (r2) => {
          ReadableStreamDefaultControllerError(branch1._readableStreamController, r2);
          ReadableStreamDefaultControllerError(branch2._readableStreamController, r2);
          if (!canceled1 || !canceled2) {
            resolveCancelPromise(void 0);
          }
          return null;
        });
        return [branch1, branch2];
      }
      function ReadableByteStreamTee(stream) {
        let reader = AcquireReadableStreamDefaultReader(stream);
        let reading = false;
        let readAgainForBranch1 = false;
        let readAgainForBranch2 = false;
        let canceled1 = false;
        let canceled2 = false;
        let reason1;
        let reason2;
        let branch1;
        let branch2;
        let resolveCancelPromise;
        const cancelPromise = newPromise((resolve) => {
          resolveCancelPromise = resolve;
        });
        function forwardReaderError(thisReader) {
          uponRejection(thisReader._closedPromise, (r2) => {
            if (thisReader !== reader) {
              return null;
            }
            ReadableByteStreamControllerError(branch1._readableStreamController, r2);
            ReadableByteStreamControllerError(branch2._readableStreamController, r2);
            if (!canceled1 || !canceled2) {
              resolveCancelPromise(void 0);
            }
            return null;
          });
        }
        function pullWithDefaultReader() {
          if (IsReadableStreamBYOBReader(reader)) {
            ReadableStreamReaderGenericRelease(reader);
            reader = AcquireReadableStreamDefaultReader(stream);
            forwardReaderError(reader);
          }
          const readRequest = {
            _chunkSteps: (chunk) => {
              _queueMicrotask(() => {
                readAgainForBranch1 = false;
                readAgainForBranch2 = false;
                const chunk1 = chunk;
                let chunk2 = chunk;
                if (!canceled1 && !canceled2) {
                  try {
                    chunk2 = CloneAsUint8Array(chunk);
                  } catch (cloneE) {
                    ReadableByteStreamControllerError(branch1._readableStreamController, cloneE);
                    ReadableByteStreamControllerError(branch2._readableStreamController, cloneE);
                    resolveCancelPromise(ReadableStreamCancel(stream, cloneE));
                    return;
                  }
                }
                if (!canceled1) {
                  ReadableByteStreamControllerEnqueue(branch1._readableStreamController, chunk1);
                }
                if (!canceled2) {
                  ReadableByteStreamControllerEnqueue(branch2._readableStreamController, chunk2);
                }
                reading = false;
                if (readAgainForBranch1) {
                  pull1Algorithm();
                } else if (readAgainForBranch2) {
                  pull2Algorithm();
                }
              });
            },
            _closeSteps: () => {
              reading = false;
              if (!canceled1) {
                ReadableByteStreamControllerClose(branch1._readableStreamController);
              }
              if (!canceled2) {
                ReadableByteStreamControllerClose(branch2._readableStreamController);
              }
              if (branch1._readableStreamController._pendingPullIntos.length > 0) {
                ReadableByteStreamControllerRespond(branch1._readableStreamController, 0);
              }
              if (branch2._readableStreamController._pendingPullIntos.length > 0) {
                ReadableByteStreamControllerRespond(branch2._readableStreamController, 0);
              }
              if (!canceled1 || !canceled2) {
                resolveCancelPromise(void 0);
              }
            },
            _errorSteps: () => {
              reading = false;
            }
          };
          ReadableStreamDefaultReaderRead(reader, readRequest);
        }
        function pullWithBYOBReader(view, forBranch2) {
          if (IsReadableStreamDefaultReader(reader)) {
            ReadableStreamReaderGenericRelease(reader);
            reader = AcquireReadableStreamBYOBReader(stream);
            forwardReaderError(reader);
          }
          const byobBranch = forBranch2 ? branch2 : branch1;
          const otherBranch = forBranch2 ? branch1 : branch2;
          const readIntoRequest = {
            _chunkSteps: (chunk) => {
              _queueMicrotask(() => {
                readAgainForBranch1 = false;
                readAgainForBranch2 = false;
                const byobCanceled = forBranch2 ? canceled2 : canceled1;
                const otherCanceled = forBranch2 ? canceled1 : canceled2;
                if (!otherCanceled) {
                  let clonedChunk;
                  try {
                    clonedChunk = CloneAsUint8Array(chunk);
                  } catch (cloneE) {
                    ReadableByteStreamControllerError(byobBranch._readableStreamController, cloneE);
                    ReadableByteStreamControllerError(otherBranch._readableStreamController, cloneE);
                    resolveCancelPromise(ReadableStreamCancel(stream, cloneE));
                    return;
                  }
                  if (!byobCanceled) {
                    ReadableByteStreamControllerRespondWithNewView(byobBranch._readableStreamController, chunk);
                  }
                  ReadableByteStreamControllerEnqueue(otherBranch._readableStreamController, clonedChunk);
                } else if (!byobCanceled) {
                  ReadableByteStreamControllerRespondWithNewView(byobBranch._readableStreamController, chunk);
                }
                reading = false;
                if (readAgainForBranch1) {
                  pull1Algorithm();
                } else if (readAgainForBranch2) {
                  pull2Algorithm();
                }
              });
            },
            _closeSteps: (chunk) => {
              reading = false;
              const byobCanceled = forBranch2 ? canceled2 : canceled1;
              const otherCanceled = forBranch2 ? canceled1 : canceled2;
              if (!byobCanceled) {
                ReadableByteStreamControllerClose(byobBranch._readableStreamController);
              }
              if (!otherCanceled) {
                ReadableByteStreamControllerClose(otherBranch._readableStreamController);
              }
              if (chunk !== void 0) {
                if (!byobCanceled) {
                  ReadableByteStreamControllerRespondWithNewView(byobBranch._readableStreamController, chunk);
                }
                if (!otherCanceled && otherBranch._readableStreamController._pendingPullIntos.length > 0) {
                  ReadableByteStreamControllerRespond(otherBranch._readableStreamController, 0);
                }
              }
              if (!byobCanceled || !otherCanceled) {
                resolveCancelPromise(void 0);
              }
            },
            _errorSteps: () => {
              reading = false;
            }
          };
          ReadableStreamBYOBReaderRead(reader, view, 1, readIntoRequest);
        }
        function pull1Algorithm() {
          if (reading) {
            readAgainForBranch1 = true;
            return promiseResolvedWith(void 0);
          }
          reading = true;
          const byobRequest = ReadableByteStreamControllerGetBYOBRequest(branch1._readableStreamController);
          if (byobRequest === null) {
            pullWithDefaultReader();
          } else {
            pullWithBYOBReader(byobRequest._view, false);
          }
          return promiseResolvedWith(void 0);
        }
        function pull2Algorithm() {
          if (reading) {
            readAgainForBranch2 = true;
            return promiseResolvedWith(void 0);
          }
          reading = true;
          const byobRequest = ReadableByteStreamControllerGetBYOBRequest(branch2._readableStreamController);
          if (byobRequest === null) {
            pullWithDefaultReader();
          } else {
            pullWithBYOBReader(byobRequest._view, true);
          }
          return promiseResolvedWith(void 0);
        }
        function cancel1Algorithm(reason) {
          canceled1 = true;
          reason1 = reason;
          if (canceled2) {
            const compositeReason = CreateArrayFromList([reason1, reason2]);
            const cancelResult = ReadableStreamCancel(stream, compositeReason);
            resolveCancelPromise(cancelResult);
          }
          return cancelPromise;
        }
        function cancel2Algorithm(reason) {
          canceled2 = true;
          reason2 = reason;
          if (canceled1) {
            const compositeReason = CreateArrayFromList([reason1, reason2]);
            const cancelResult = ReadableStreamCancel(stream, compositeReason);
            resolveCancelPromise(cancelResult);
          }
          return cancelPromise;
        }
        function startAlgorithm() {
          return;
        }
        branch1 = CreateReadableByteStream(startAlgorithm, pull1Algorithm, cancel1Algorithm);
        branch2 = CreateReadableByteStream(startAlgorithm, pull2Algorithm, cancel2Algorithm);
        forwardReaderError(reader);
        return [branch1, branch2];
      }
      function isReadableStreamLike(stream) {
        return typeIsObject(stream) && typeof stream.getReader !== "undefined";
      }
      function ReadableStreamFrom(source) {
        if (isReadableStreamLike(source)) {
          return ReadableStreamFromDefaultReader(source.getReader());
        }
        return ReadableStreamFromIterable(source);
      }
      function ReadableStreamFromIterable(asyncIterable) {
        let stream;
        const iteratorRecord = GetIterator(asyncIterable, "async");
        const startAlgorithm = noop2;
        function pullAlgorithm() {
          let nextResult;
          try {
            nextResult = IteratorNext(iteratorRecord);
          } catch (e2) {
            return promiseRejectedWith(e2);
          }
          const nextPromise = promiseResolvedWith(nextResult);
          return transformPromiseWith(nextPromise, (iterResult) => {
            if (!typeIsObject(iterResult)) {
              throw new TypeError("The promise returned by the iterator.next() method must fulfill with an object");
            }
            const done = IteratorComplete(iterResult);
            if (done) {
              ReadableStreamDefaultControllerClose(stream._readableStreamController);
            } else {
              const value = IteratorValue(iterResult);
              ReadableStreamDefaultControllerEnqueue(stream._readableStreamController, value);
            }
          });
        }
        function cancelAlgorithm(reason) {
          const iterator = iteratorRecord.iterator;
          let returnMethod;
          try {
            returnMethod = GetMethod(iterator, "return");
          } catch (e2) {
            return promiseRejectedWith(e2);
          }
          if (returnMethod === void 0) {
            return promiseResolvedWith(void 0);
          }
          let returnResult;
          try {
            returnResult = reflectCall(returnMethod, iterator, [reason]);
          } catch (e2) {
            return promiseRejectedWith(e2);
          }
          const returnPromise = promiseResolvedWith(returnResult);
          return transformPromiseWith(returnPromise, (iterResult) => {
            if (!typeIsObject(iterResult)) {
              throw new TypeError("The promise returned by the iterator.return() method must fulfill with an object");
            }
            return void 0;
          });
        }
        stream = CreateReadableStream(startAlgorithm, pullAlgorithm, cancelAlgorithm, 0);
        return stream;
      }
      function ReadableStreamFromDefaultReader(reader) {
        let stream;
        const startAlgorithm = noop2;
        function pullAlgorithm() {
          let readPromise;
          try {
            readPromise = reader.read();
          } catch (e2) {
            return promiseRejectedWith(e2);
          }
          return transformPromiseWith(readPromise, (readResult) => {
            if (!typeIsObject(readResult)) {
              throw new TypeError("The promise returned by the reader.read() method must fulfill with an object");
            }
            if (readResult.done) {
              ReadableStreamDefaultControllerClose(stream._readableStreamController);
            } else {
              const value = readResult.value;
              ReadableStreamDefaultControllerEnqueue(stream._readableStreamController, value);
            }
          });
        }
        function cancelAlgorithm(reason) {
          try {
            return promiseResolvedWith(reader.cancel(reason));
          } catch (e2) {
            return promiseRejectedWith(e2);
          }
        }
        stream = CreateReadableStream(startAlgorithm, pullAlgorithm, cancelAlgorithm, 0);
        return stream;
      }
      function convertUnderlyingDefaultOrByteSource(source, context) {
        assertDictionary(source, context);
        const original = source;
        const autoAllocateChunkSize = original === null || original === void 0 ? void 0 : original.autoAllocateChunkSize;
        const cancel = original === null || original === void 0 ? void 0 : original.cancel;
        const pull = original === null || original === void 0 ? void 0 : original.pull;
        const start = original === null || original === void 0 ? void 0 : original.start;
        const type = original === null || original === void 0 ? void 0 : original.type;
        return {
          autoAllocateChunkSize: autoAllocateChunkSize === void 0 ? void 0 : convertUnsignedLongLongWithEnforceRange(autoAllocateChunkSize, `${context} has member 'autoAllocateChunkSize' that`),
          cancel: cancel === void 0 ? void 0 : convertUnderlyingSourceCancelCallback(cancel, original, `${context} has member 'cancel' that`),
          pull: pull === void 0 ? void 0 : convertUnderlyingSourcePullCallback(pull, original, `${context} has member 'pull' that`),
          start: start === void 0 ? void 0 : convertUnderlyingSourceStartCallback(start, original, `${context} has member 'start' that`),
          type: type === void 0 ? void 0 : convertReadableStreamType(type, `${context} has member 'type' that`)
        };
      }
      function convertUnderlyingSourceCancelCallback(fn, original, context) {
        assertFunction(fn, context);
        return (reason) => promiseCall(fn, original, [reason]);
      }
      function convertUnderlyingSourcePullCallback(fn, original, context) {
        assertFunction(fn, context);
        return (controller) => promiseCall(fn, original, [controller]);
      }
      function convertUnderlyingSourceStartCallback(fn, original, context) {
        assertFunction(fn, context);
        return (controller) => reflectCall(fn, original, [controller]);
      }
      function convertReadableStreamType(type, context) {
        type = `${type}`;
        if (type !== "bytes") {
          throw new TypeError(`${context} '${type}' is not a valid enumeration value for ReadableStreamType`);
        }
        return type;
      }
      function convertIteratorOptions(options, context) {
        assertDictionary(options, context);
        const preventCancel = options === null || options === void 0 ? void 0 : options.preventCancel;
        return { preventCancel: Boolean(preventCancel) };
      }
      function convertPipeOptions(options, context) {
        assertDictionary(options, context);
        const preventAbort = options === null || options === void 0 ? void 0 : options.preventAbort;
        const preventCancel = options === null || options === void 0 ? void 0 : options.preventCancel;
        const preventClose = options === null || options === void 0 ? void 0 : options.preventClose;
        const signal = options === null || options === void 0 ? void 0 : options.signal;
        if (signal !== void 0) {
          assertAbortSignal(signal, `${context} has member 'signal' that`);
        }
        return {
          preventAbort: Boolean(preventAbort),
          preventCancel: Boolean(preventCancel),
          preventClose: Boolean(preventClose),
          signal
        };
      }
      function assertAbortSignal(signal, context) {
        if (!isAbortSignal2(signal)) {
          throw new TypeError(`${context} is not an AbortSignal.`);
        }
      }
      function convertReadableWritablePair(pair, context) {
        assertDictionary(pair, context);
        const readable = pair === null || pair === void 0 ? void 0 : pair.readable;
        assertRequiredField(readable, "readable", "ReadableWritablePair");
        assertReadableStream(readable, `${context} has member 'readable' that`);
        const writable = pair === null || pair === void 0 ? void 0 : pair.writable;
        assertRequiredField(writable, "writable", "ReadableWritablePair");
        assertWritableStream(writable, `${context} has member 'writable' that`);
        return { readable, writable };
      }
      class ReadableStream2 {
        constructor(rawUnderlyingSource = {}, rawStrategy = {}) {
          if (rawUnderlyingSource === void 0) {
            rawUnderlyingSource = null;
          } else {
            assertObject(rawUnderlyingSource, "First parameter");
          }
          const strategy = convertQueuingStrategy(rawStrategy, "Second parameter");
          const underlyingSource = convertUnderlyingDefaultOrByteSource(rawUnderlyingSource, "First parameter");
          InitializeReadableStream(this);
          if (underlyingSource.type === "bytes") {
            if (strategy.size !== void 0) {
              throw new RangeError("The strategy for a byte stream cannot have a size function");
            }
            const highWaterMark = ExtractHighWaterMark(strategy, 0);
            SetUpReadableByteStreamControllerFromUnderlyingSource(this, underlyingSource, highWaterMark);
          } else {
            const sizeAlgorithm = ExtractSizeAlgorithm(strategy);
            const highWaterMark = ExtractHighWaterMark(strategy, 1);
            SetUpReadableStreamDefaultControllerFromUnderlyingSource(this, underlyingSource, highWaterMark, sizeAlgorithm);
          }
        }
        /**
         * Whether or not the readable stream is locked to a {@link ReadableStreamDefaultReader | reader}.
         */
        get locked() {
          if (!IsReadableStream(this)) {
            throw streamBrandCheckException$1("locked");
          }
          return IsReadableStreamLocked(this);
        }
        /**
         * Cancels the stream, signaling a loss of interest in the stream by a consumer.
         *
         * The supplied `reason` argument will be given to the underlying source's {@link UnderlyingSource.cancel | cancel()}
         * method, which might or might not use it.
         */
        cancel(reason = void 0) {
          if (!IsReadableStream(this)) {
            return promiseRejectedWith(streamBrandCheckException$1("cancel"));
          }
          if (IsReadableStreamLocked(this)) {
            return promiseRejectedWith(new TypeError("Cannot cancel a stream that already has a reader"));
          }
          return ReadableStreamCancel(this, reason);
        }
        getReader(rawOptions = void 0) {
          if (!IsReadableStream(this)) {
            throw streamBrandCheckException$1("getReader");
          }
          const options = convertReaderOptions(rawOptions, "First parameter");
          if (options.mode === void 0) {
            return AcquireReadableStreamDefaultReader(this);
          }
          return AcquireReadableStreamBYOBReader(this);
        }
        pipeThrough(rawTransform, rawOptions = {}) {
          if (!IsReadableStream(this)) {
            throw streamBrandCheckException$1("pipeThrough");
          }
          assertRequiredArgument(rawTransform, 1, "pipeThrough");
          const transform = convertReadableWritablePair(rawTransform, "First parameter");
          const options = convertPipeOptions(rawOptions, "Second parameter");
          if (IsReadableStreamLocked(this)) {
            throw new TypeError("ReadableStream.prototype.pipeThrough cannot be used on a locked ReadableStream");
          }
          if (IsWritableStreamLocked(transform.writable)) {
            throw new TypeError("ReadableStream.prototype.pipeThrough cannot be used on a locked WritableStream");
          }
          const promise = ReadableStreamPipeTo(this, transform.writable, options.preventClose, options.preventAbort, options.preventCancel, options.signal);
          setPromiseIsHandledToTrue(promise);
          return transform.readable;
        }
        pipeTo(destination, rawOptions = {}) {
          if (!IsReadableStream(this)) {
            return promiseRejectedWith(streamBrandCheckException$1("pipeTo"));
          }
          if (destination === void 0) {
            return promiseRejectedWith(`Parameter 1 is required in 'pipeTo'.`);
          }
          if (!IsWritableStream(destination)) {
            return promiseRejectedWith(new TypeError(`ReadableStream.prototype.pipeTo's first argument must be a WritableStream`));
          }
          let options;
          try {
            options = convertPipeOptions(rawOptions, "Second parameter");
          } catch (e2) {
            return promiseRejectedWith(e2);
          }
          if (IsReadableStreamLocked(this)) {
            return promiseRejectedWith(new TypeError("ReadableStream.prototype.pipeTo cannot be used on a locked ReadableStream"));
          }
          if (IsWritableStreamLocked(destination)) {
            return promiseRejectedWith(new TypeError("ReadableStream.prototype.pipeTo cannot be used on a locked WritableStream"));
          }
          return ReadableStreamPipeTo(this, destination, options.preventClose, options.preventAbort, options.preventCancel, options.signal);
        }
        /**
         * Tees this readable stream, returning a two-element array containing the two resulting branches as
         * new {@link ReadableStream} instances.
         *
         * Teeing a stream will lock it, preventing any other consumer from acquiring a reader.
         * To cancel the stream, cancel both of the resulting branches; a composite cancellation reason will then be
         * propagated to the stream's underlying source.
         *
         * Note that the chunks seen in each branch will be the same object. If the chunks are not immutable,
         * this could allow interference between the two branches.
         */
        tee() {
          if (!IsReadableStream(this)) {
            throw streamBrandCheckException$1("tee");
          }
          const branches = ReadableStreamTee(this);
          return CreateArrayFromList(branches);
        }
        values(rawOptions = void 0) {
          if (!IsReadableStream(this)) {
            throw streamBrandCheckException$1("values");
          }
          const options = convertIteratorOptions(rawOptions, "First parameter");
          return AcquireReadableStreamAsyncIterator(this, options.preventCancel);
        }
        [SymbolAsyncIterator](options) {
          return this.values(options);
        }
        /**
         * Creates a new ReadableStream wrapping the provided iterable or async iterable.
         *
         * This can be used to adapt various kinds of objects into a readable stream,
         * such as an array, an async generator, or a Node.js readable stream.
         */
        static from(asyncIterable) {
          return ReadableStreamFrom(asyncIterable);
        }
      }
      Object.defineProperties(ReadableStream2, {
        from: { enumerable: true }
      });
      Object.defineProperties(ReadableStream2.prototype, {
        cancel: { enumerable: true },
        getReader: { enumerable: true },
        pipeThrough: { enumerable: true },
        pipeTo: { enumerable: true },
        tee: { enumerable: true },
        values: { enumerable: true },
        locked: { enumerable: true }
      });
      setFunctionName(ReadableStream2.from, "from");
      setFunctionName(ReadableStream2.prototype.cancel, "cancel");
      setFunctionName(ReadableStream2.prototype.getReader, "getReader");
      setFunctionName(ReadableStream2.prototype.pipeThrough, "pipeThrough");
      setFunctionName(ReadableStream2.prototype.pipeTo, "pipeTo");
      setFunctionName(ReadableStream2.prototype.tee, "tee");
      setFunctionName(ReadableStream2.prototype.values, "values");
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(ReadableStream2.prototype, Symbol.toStringTag, {
          value: "ReadableStream",
          configurable: true
        });
      }
      Object.defineProperty(ReadableStream2.prototype, SymbolAsyncIterator, {
        value: ReadableStream2.prototype.values,
        writable: true,
        configurable: true
      });
      function CreateReadableStream(startAlgorithm, pullAlgorithm, cancelAlgorithm, highWaterMark = 1, sizeAlgorithm = () => 1) {
        const stream = Object.create(ReadableStream2.prototype);
        InitializeReadableStream(stream);
        const controller = Object.create(ReadableStreamDefaultController.prototype);
        SetUpReadableStreamDefaultController(stream, controller, startAlgorithm, pullAlgorithm, cancelAlgorithm, highWaterMark, sizeAlgorithm);
        return stream;
      }
      function CreateReadableByteStream(startAlgorithm, pullAlgorithm, cancelAlgorithm) {
        const stream = Object.create(ReadableStream2.prototype);
        InitializeReadableStream(stream);
        const controller = Object.create(ReadableByteStreamController.prototype);
        SetUpReadableByteStreamController(stream, controller, startAlgorithm, pullAlgorithm, cancelAlgorithm, 0, void 0);
        return stream;
      }
      function InitializeReadableStream(stream) {
        stream._state = "readable";
        stream._reader = void 0;
        stream._storedError = void 0;
        stream._disturbed = false;
      }
      function IsReadableStream(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_readableStreamController")) {
          return false;
        }
        return x2 instanceof ReadableStream2;
      }
      function IsReadableStreamLocked(stream) {
        if (stream._reader === void 0) {
          return false;
        }
        return true;
      }
      function ReadableStreamCancel(stream, reason) {
        stream._disturbed = true;
        if (stream._state === "closed") {
          return promiseResolvedWith(void 0);
        }
        if (stream._state === "errored") {
          return promiseRejectedWith(stream._storedError);
        }
        ReadableStreamClose(stream);
        const reader = stream._reader;
        if (reader !== void 0 && IsReadableStreamBYOBReader(reader)) {
          const readIntoRequests = reader._readIntoRequests;
          reader._readIntoRequests = new SimpleQueue();
          readIntoRequests.forEach((readIntoRequest) => {
            readIntoRequest._closeSteps(void 0);
          });
        }
        const sourceCancelPromise = stream._readableStreamController[CancelSteps](reason);
        return transformPromiseWith(sourceCancelPromise, noop2);
      }
      function ReadableStreamClose(stream) {
        stream._state = "closed";
        const reader = stream._reader;
        if (reader === void 0) {
          return;
        }
        defaultReaderClosedPromiseResolve(reader);
        if (IsReadableStreamDefaultReader(reader)) {
          const readRequests = reader._readRequests;
          reader._readRequests = new SimpleQueue();
          readRequests.forEach((readRequest) => {
            readRequest._closeSteps();
          });
        }
      }
      function ReadableStreamError(stream, e2) {
        stream._state = "errored";
        stream._storedError = e2;
        const reader = stream._reader;
        if (reader === void 0) {
          return;
        }
        defaultReaderClosedPromiseReject(reader, e2);
        if (IsReadableStreamDefaultReader(reader)) {
          ReadableStreamDefaultReaderErrorReadRequests(reader, e2);
        } else {
          ReadableStreamBYOBReaderErrorReadIntoRequests(reader, e2);
        }
      }
      function streamBrandCheckException$1(name) {
        return new TypeError(`ReadableStream.prototype.${name} can only be used on a ReadableStream`);
      }
      function convertQueuingStrategyInit(init, context) {
        assertDictionary(init, context);
        const highWaterMark = init === null || init === void 0 ? void 0 : init.highWaterMark;
        assertRequiredField(highWaterMark, "highWaterMark", "QueuingStrategyInit");
        return {
          highWaterMark: convertUnrestrictedDouble(highWaterMark)
        };
      }
      const byteLengthSizeFunction = (chunk) => {
        return chunk.byteLength;
      };
      setFunctionName(byteLengthSizeFunction, "size");
      class ByteLengthQueuingStrategy {
        constructor(options) {
          assertRequiredArgument(options, 1, "ByteLengthQueuingStrategy");
          options = convertQueuingStrategyInit(options, "First parameter");
          this._byteLengthQueuingStrategyHighWaterMark = options.highWaterMark;
        }
        /**
         * Returns the high water mark provided to the constructor.
         */
        get highWaterMark() {
          if (!IsByteLengthQueuingStrategy(this)) {
            throw byteLengthBrandCheckException("highWaterMark");
          }
          return this._byteLengthQueuingStrategyHighWaterMark;
        }
        /**
         * Measures the size of `chunk` by returning the value of its `byteLength` property.
         */
        get size() {
          if (!IsByteLengthQueuingStrategy(this)) {
            throw byteLengthBrandCheckException("size");
          }
          return byteLengthSizeFunction;
        }
      }
      Object.defineProperties(ByteLengthQueuingStrategy.prototype, {
        highWaterMark: { enumerable: true },
        size: { enumerable: true }
      });
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(ByteLengthQueuingStrategy.prototype, Symbol.toStringTag, {
          value: "ByteLengthQueuingStrategy",
          configurable: true
        });
      }
      function byteLengthBrandCheckException(name) {
        return new TypeError(`ByteLengthQueuingStrategy.prototype.${name} can only be used on a ByteLengthQueuingStrategy`);
      }
      function IsByteLengthQueuingStrategy(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_byteLengthQueuingStrategyHighWaterMark")) {
          return false;
        }
        return x2 instanceof ByteLengthQueuingStrategy;
      }
      const countSizeFunction = () => {
        return 1;
      };
      setFunctionName(countSizeFunction, "size");
      class CountQueuingStrategy {
        constructor(options) {
          assertRequiredArgument(options, 1, "CountQueuingStrategy");
          options = convertQueuingStrategyInit(options, "First parameter");
          this._countQueuingStrategyHighWaterMark = options.highWaterMark;
        }
        /**
         * Returns the high water mark provided to the constructor.
         */
        get highWaterMark() {
          if (!IsCountQueuingStrategy(this)) {
            throw countBrandCheckException("highWaterMark");
          }
          return this._countQueuingStrategyHighWaterMark;
        }
        /**
         * Measures the size of `chunk` by always returning 1.
         * This ensures that the total queue size is a count of the number of chunks in the queue.
         */
        get size() {
          if (!IsCountQueuingStrategy(this)) {
            throw countBrandCheckException("size");
          }
          return countSizeFunction;
        }
      }
      Object.defineProperties(CountQueuingStrategy.prototype, {
        highWaterMark: { enumerable: true },
        size: { enumerable: true }
      });
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(CountQueuingStrategy.prototype, Symbol.toStringTag, {
          value: "CountQueuingStrategy",
          configurable: true
        });
      }
      function countBrandCheckException(name) {
        return new TypeError(`CountQueuingStrategy.prototype.${name} can only be used on a CountQueuingStrategy`);
      }
      function IsCountQueuingStrategy(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_countQueuingStrategyHighWaterMark")) {
          return false;
        }
        return x2 instanceof CountQueuingStrategy;
      }
      function convertTransformer(original, context) {
        assertDictionary(original, context);
        const cancel = original === null || original === void 0 ? void 0 : original.cancel;
        const flush = original === null || original === void 0 ? void 0 : original.flush;
        const readableType = original === null || original === void 0 ? void 0 : original.readableType;
        const start = original === null || original === void 0 ? void 0 : original.start;
        const transform = original === null || original === void 0 ? void 0 : original.transform;
        const writableType = original === null || original === void 0 ? void 0 : original.writableType;
        return {
          cancel: cancel === void 0 ? void 0 : convertTransformerCancelCallback(cancel, original, `${context} has member 'cancel' that`),
          flush: flush === void 0 ? void 0 : convertTransformerFlushCallback(flush, original, `${context} has member 'flush' that`),
          readableType,
          start: start === void 0 ? void 0 : convertTransformerStartCallback(start, original, `${context} has member 'start' that`),
          transform: transform === void 0 ? void 0 : convertTransformerTransformCallback(transform, original, `${context} has member 'transform' that`),
          writableType
        };
      }
      function convertTransformerFlushCallback(fn, original, context) {
        assertFunction(fn, context);
        return (controller) => promiseCall(fn, original, [controller]);
      }
      function convertTransformerStartCallback(fn, original, context) {
        assertFunction(fn, context);
        return (controller) => reflectCall(fn, original, [controller]);
      }
      function convertTransformerTransformCallback(fn, original, context) {
        assertFunction(fn, context);
        return (chunk, controller) => promiseCall(fn, original, [chunk, controller]);
      }
      function convertTransformerCancelCallback(fn, original, context) {
        assertFunction(fn, context);
        return (reason) => promiseCall(fn, original, [reason]);
      }
      class TransformStream {
        constructor(rawTransformer = {}, rawWritableStrategy = {}, rawReadableStrategy = {}) {
          if (rawTransformer === void 0) {
            rawTransformer = null;
          }
          const writableStrategy = convertQueuingStrategy(rawWritableStrategy, "Second parameter");
          const readableStrategy = convertQueuingStrategy(rawReadableStrategy, "Third parameter");
          const transformer = convertTransformer(rawTransformer, "First parameter");
          if (transformer.readableType !== void 0) {
            throw new RangeError("Invalid readableType specified");
          }
          if (transformer.writableType !== void 0) {
            throw new RangeError("Invalid writableType specified");
          }
          const readableHighWaterMark = ExtractHighWaterMark(readableStrategy, 0);
          const readableSizeAlgorithm = ExtractSizeAlgorithm(readableStrategy);
          const writableHighWaterMark = ExtractHighWaterMark(writableStrategy, 1);
          const writableSizeAlgorithm = ExtractSizeAlgorithm(writableStrategy);
          let startPromise_resolve;
          const startPromise = newPromise((resolve) => {
            startPromise_resolve = resolve;
          });
          InitializeTransformStream(this, startPromise, writableHighWaterMark, writableSizeAlgorithm, readableHighWaterMark, readableSizeAlgorithm);
          SetUpTransformStreamDefaultControllerFromTransformer(this, transformer);
          if (transformer.start !== void 0) {
            startPromise_resolve(transformer.start(this._transformStreamController));
          } else {
            startPromise_resolve(void 0);
          }
        }
        /**
         * The readable side of the transform stream.
         */
        get readable() {
          if (!IsTransformStream(this)) {
            throw streamBrandCheckException("readable");
          }
          return this._readable;
        }
        /**
         * The writable side of the transform stream.
         */
        get writable() {
          if (!IsTransformStream(this)) {
            throw streamBrandCheckException("writable");
          }
          return this._writable;
        }
      }
      Object.defineProperties(TransformStream.prototype, {
        readable: { enumerable: true },
        writable: { enumerable: true }
      });
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(TransformStream.prototype, Symbol.toStringTag, {
          value: "TransformStream",
          configurable: true
        });
      }
      function InitializeTransformStream(stream, startPromise, writableHighWaterMark, writableSizeAlgorithm, readableHighWaterMark, readableSizeAlgorithm) {
        function startAlgorithm() {
          return startPromise;
        }
        function writeAlgorithm(chunk) {
          return TransformStreamDefaultSinkWriteAlgorithm(stream, chunk);
        }
        function abortAlgorithm(reason) {
          return TransformStreamDefaultSinkAbortAlgorithm(stream, reason);
        }
        function closeAlgorithm() {
          return TransformStreamDefaultSinkCloseAlgorithm(stream);
        }
        stream._writable = CreateWritableStream(startAlgorithm, writeAlgorithm, closeAlgorithm, abortAlgorithm, writableHighWaterMark, writableSizeAlgorithm);
        function pullAlgorithm() {
          return TransformStreamDefaultSourcePullAlgorithm(stream);
        }
        function cancelAlgorithm(reason) {
          return TransformStreamDefaultSourceCancelAlgorithm(stream, reason);
        }
        stream._readable = CreateReadableStream(startAlgorithm, pullAlgorithm, cancelAlgorithm, readableHighWaterMark, readableSizeAlgorithm);
        stream._backpressure = void 0;
        stream._backpressureChangePromise = void 0;
        stream._backpressureChangePromise_resolve = void 0;
        TransformStreamSetBackpressure(stream, true);
        stream._transformStreamController = void 0;
      }
      function IsTransformStream(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_transformStreamController")) {
          return false;
        }
        return x2 instanceof TransformStream;
      }
      function TransformStreamError(stream, e2) {
        ReadableStreamDefaultControllerError(stream._readable._readableStreamController, e2);
        TransformStreamErrorWritableAndUnblockWrite(stream, e2);
      }
      function TransformStreamErrorWritableAndUnblockWrite(stream, e2) {
        TransformStreamDefaultControllerClearAlgorithms(stream._transformStreamController);
        WritableStreamDefaultControllerErrorIfNeeded(stream._writable._writableStreamController, e2);
        TransformStreamUnblockWrite(stream);
      }
      function TransformStreamUnblockWrite(stream) {
        if (stream._backpressure) {
          TransformStreamSetBackpressure(stream, false);
        }
      }
      function TransformStreamSetBackpressure(stream, backpressure) {
        if (stream._backpressureChangePromise !== void 0) {
          stream._backpressureChangePromise_resolve();
        }
        stream._backpressureChangePromise = newPromise((resolve) => {
          stream._backpressureChangePromise_resolve = resolve;
        });
        stream._backpressure = backpressure;
      }
      class TransformStreamDefaultController {
        constructor() {
          throw new TypeError("Illegal constructor");
        }
        /**
         * Returns the desired size to fill the readable side’s internal queue. It can be negative, if the queue is over-full.
         */
        get desiredSize() {
          if (!IsTransformStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException("desiredSize");
          }
          const readableController = this._controlledTransformStream._readable._readableStreamController;
          return ReadableStreamDefaultControllerGetDesiredSize(readableController);
        }
        enqueue(chunk = void 0) {
          if (!IsTransformStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException("enqueue");
          }
          TransformStreamDefaultControllerEnqueue(this, chunk);
        }
        /**
         * Errors both the readable side and the writable side of the controlled transform stream, making all future
         * interactions with it fail with the given error `e`. Any chunks queued for transformation will be discarded.
         */
        error(reason = void 0) {
          if (!IsTransformStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException("error");
          }
          TransformStreamDefaultControllerError(this, reason);
        }
        /**
         * Closes the readable side and errors the writable side of the controlled transform stream. This is useful when the
         * transformer only needs to consume a portion of the chunks written to the writable side.
         */
        terminate() {
          if (!IsTransformStreamDefaultController(this)) {
            throw defaultControllerBrandCheckException("terminate");
          }
          TransformStreamDefaultControllerTerminate(this);
        }
      }
      Object.defineProperties(TransformStreamDefaultController.prototype, {
        enqueue: { enumerable: true },
        error: { enumerable: true },
        terminate: { enumerable: true },
        desiredSize: { enumerable: true }
      });
      setFunctionName(TransformStreamDefaultController.prototype.enqueue, "enqueue");
      setFunctionName(TransformStreamDefaultController.prototype.error, "error");
      setFunctionName(TransformStreamDefaultController.prototype.terminate, "terminate");
      if (typeof Symbol.toStringTag === "symbol") {
        Object.defineProperty(TransformStreamDefaultController.prototype, Symbol.toStringTag, {
          value: "TransformStreamDefaultController",
          configurable: true
        });
      }
      function IsTransformStreamDefaultController(x2) {
        if (!typeIsObject(x2)) {
          return false;
        }
        if (!Object.prototype.hasOwnProperty.call(x2, "_controlledTransformStream")) {
          return false;
        }
        return x2 instanceof TransformStreamDefaultController;
      }
      function SetUpTransformStreamDefaultController(stream, controller, transformAlgorithm, flushAlgorithm, cancelAlgorithm) {
        controller._controlledTransformStream = stream;
        stream._transformStreamController = controller;
        controller._transformAlgorithm = transformAlgorithm;
        controller._flushAlgorithm = flushAlgorithm;
        controller._cancelAlgorithm = cancelAlgorithm;
        controller._finishPromise = void 0;
        controller._finishPromise_resolve = void 0;
        controller._finishPromise_reject = void 0;
      }
      function SetUpTransformStreamDefaultControllerFromTransformer(stream, transformer) {
        const controller = Object.create(TransformStreamDefaultController.prototype);
        let transformAlgorithm;
        let flushAlgorithm;
        let cancelAlgorithm;
        if (transformer.transform !== void 0) {
          transformAlgorithm = (chunk) => transformer.transform(chunk, controller);
        } else {
          transformAlgorithm = (chunk) => {
            try {
              TransformStreamDefaultControllerEnqueue(controller, chunk);
              return promiseResolvedWith(void 0);
            } catch (transformResultE) {
              return promiseRejectedWith(transformResultE);
            }
          };
        }
        if (transformer.flush !== void 0) {
          flushAlgorithm = () => transformer.flush(controller);
        } else {
          flushAlgorithm = () => promiseResolvedWith(void 0);
        }
        if (transformer.cancel !== void 0) {
          cancelAlgorithm = (reason) => transformer.cancel(reason);
        } else {
          cancelAlgorithm = () => promiseResolvedWith(void 0);
        }
        SetUpTransformStreamDefaultController(stream, controller, transformAlgorithm, flushAlgorithm, cancelAlgorithm);
      }
      function TransformStreamDefaultControllerClearAlgorithms(controller) {
        controller._transformAlgorithm = void 0;
        controller._flushAlgorithm = void 0;
        controller._cancelAlgorithm = void 0;
      }
      function TransformStreamDefaultControllerEnqueue(controller, chunk) {
        const stream = controller._controlledTransformStream;
        const readableController = stream._readable._readableStreamController;
        if (!ReadableStreamDefaultControllerCanCloseOrEnqueue(readableController)) {
          throw new TypeError("Readable side is not in a state that permits enqueue");
        }
        try {
          ReadableStreamDefaultControllerEnqueue(readableController, chunk);
        } catch (e2) {
          TransformStreamErrorWritableAndUnblockWrite(stream, e2);
          throw stream._readable._storedError;
        }
        const backpressure = ReadableStreamDefaultControllerHasBackpressure(readableController);
        if (backpressure !== stream._backpressure) {
          TransformStreamSetBackpressure(stream, true);
        }
      }
      function TransformStreamDefaultControllerError(controller, e2) {
        TransformStreamError(controller._controlledTransformStream, e2);
      }
      function TransformStreamDefaultControllerPerformTransform(controller, chunk) {
        const transformPromise = controller._transformAlgorithm(chunk);
        return transformPromiseWith(transformPromise, void 0, (r2) => {
          TransformStreamError(controller._controlledTransformStream, r2);
          throw r2;
        });
      }
      function TransformStreamDefaultControllerTerminate(controller) {
        const stream = controller._controlledTransformStream;
        const readableController = stream._readable._readableStreamController;
        ReadableStreamDefaultControllerClose(readableController);
        const error = new TypeError("TransformStream terminated");
        TransformStreamErrorWritableAndUnblockWrite(stream, error);
      }
      function TransformStreamDefaultSinkWriteAlgorithm(stream, chunk) {
        const controller = stream._transformStreamController;
        if (stream._backpressure) {
          const backpressureChangePromise = stream._backpressureChangePromise;
          return transformPromiseWith(backpressureChangePromise, () => {
            const writable = stream._writable;
            const state = writable._state;
            if (state === "erroring") {
              throw writable._storedError;
            }
            return TransformStreamDefaultControllerPerformTransform(controller, chunk);
          });
        }
        return TransformStreamDefaultControllerPerformTransform(controller, chunk);
      }
      function TransformStreamDefaultSinkAbortAlgorithm(stream, reason) {
        const controller = stream._transformStreamController;
        if (controller._finishPromise !== void 0) {
          return controller._finishPromise;
        }
        const readable = stream._readable;
        controller._finishPromise = newPromise((resolve, reject) => {
          controller._finishPromise_resolve = resolve;
          controller._finishPromise_reject = reject;
        });
        const cancelPromise = controller._cancelAlgorithm(reason);
        TransformStreamDefaultControllerClearAlgorithms(controller);
        uponPromise(cancelPromise, () => {
          if (readable._state === "errored") {
            defaultControllerFinishPromiseReject(controller, readable._storedError);
          } else {
            ReadableStreamDefaultControllerError(readable._readableStreamController, reason);
            defaultControllerFinishPromiseResolve(controller);
          }
          return null;
        }, (r2) => {
          ReadableStreamDefaultControllerError(readable._readableStreamController, r2);
          defaultControllerFinishPromiseReject(controller, r2);
          return null;
        });
        return controller._finishPromise;
      }
      function TransformStreamDefaultSinkCloseAlgorithm(stream) {
        const controller = stream._transformStreamController;
        if (controller._finishPromise !== void 0) {
          return controller._finishPromise;
        }
        const readable = stream._readable;
        controller._finishPromise = newPromise((resolve, reject) => {
          controller._finishPromise_resolve = resolve;
          controller._finishPromise_reject = reject;
        });
        const flushPromise = controller._flushAlgorithm();
        TransformStreamDefaultControllerClearAlgorithms(controller);
        uponPromise(flushPromise, () => {
          if (readable._state === "errored") {
            defaultControllerFinishPromiseReject(controller, readable._storedError);
          } else {
            ReadableStreamDefaultControllerClose(readable._readableStreamController);
            defaultControllerFinishPromiseResolve(controller);
          }
          return null;
        }, (r2) => {
          ReadableStreamDefaultControllerError(readable._readableStreamController, r2);
          defaultControllerFinishPromiseReject(controller, r2);
          return null;
        });
        return controller._finishPromise;
      }
      function TransformStreamDefaultSourcePullAlgorithm(stream) {
        TransformStreamSetBackpressure(stream, false);
        return stream._backpressureChangePromise;
      }
      function TransformStreamDefaultSourceCancelAlgorithm(stream, reason) {
        const controller = stream._transformStreamController;
        if (controller._finishPromise !== void 0) {
          return controller._finishPromise;
        }
        const writable = stream._writable;
        controller._finishPromise = newPromise((resolve, reject) => {
          controller._finishPromise_resolve = resolve;
          controller._finishPromise_reject = reject;
        });
        const cancelPromise = controller._cancelAlgorithm(reason);
        TransformStreamDefaultControllerClearAlgorithms(controller);
        uponPromise(cancelPromise, () => {
          if (writable._state === "errored") {
            defaultControllerFinishPromiseReject(controller, writable._storedError);
          } else {
            WritableStreamDefaultControllerErrorIfNeeded(writable._writableStreamController, reason);
            TransformStreamUnblockWrite(stream);
            defaultControllerFinishPromiseResolve(controller);
          }
          return null;
        }, (r2) => {
          WritableStreamDefaultControllerErrorIfNeeded(writable._writableStreamController, r2);
          TransformStreamUnblockWrite(stream);
          defaultControllerFinishPromiseReject(controller, r2);
          return null;
        });
        return controller._finishPromise;
      }
      function defaultControllerBrandCheckException(name) {
        return new TypeError(`TransformStreamDefaultController.prototype.${name} can only be used on a TransformStreamDefaultController`);
      }
      function defaultControllerFinishPromiseResolve(controller) {
        if (controller._finishPromise_resolve === void 0) {
          return;
        }
        controller._finishPromise_resolve();
        controller._finishPromise_resolve = void 0;
        controller._finishPromise_reject = void 0;
      }
      function defaultControllerFinishPromiseReject(controller, reason) {
        if (controller._finishPromise_reject === void 0) {
          return;
        }
        setPromiseIsHandledToTrue(controller._finishPromise);
        controller._finishPromise_reject(reason);
        controller._finishPromise_resolve = void 0;
        controller._finishPromise_reject = void 0;
      }
      function streamBrandCheckException(name) {
        return new TypeError(`TransformStream.prototype.${name} can only be used on a TransformStream`);
      }
      exports2.ByteLengthQueuingStrategy = ByteLengthQueuingStrategy;
      exports2.CountQueuingStrategy = CountQueuingStrategy;
      exports2.ReadableByteStreamController = ReadableByteStreamController;
      exports2.ReadableStream = ReadableStream2;
      exports2.ReadableStreamBYOBReader = ReadableStreamBYOBReader;
      exports2.ReadableStreamBYOBRequest = ReadableStreamBYOBRequest;
      exports2.ReadableStreamDefaultController = ReadableStreamDefaultController;
      exports2.ReadableStreamDefaultReader = ReadableStreamDefaultReader;
      exports2.TransformStream = TransformStream;
      exports2.TransformStreamDefaultController = TransformStreamDefaultController;
      exports2.WritableStream = WritableStream;
      exports2.WritableStreamDefaultController = WritableStreamDefaultController;
      exports2.WritableStreamDefaultWriter = WritableStreamDefaultWriter;
    });
  }
});

// node_modules/fetch-blob/streams.cjs
var require_streams = __commonJS({
  "node_modules/fetch-blob/streams.cjs"() {
    var POOL_SIZE2 = 65536;
    if (!globalThis.ReadableStream) {
      try {
        const process2 = __require("process");
        const { emitWarning } = process2;
        try {
          process2.emitWarning = () => {
          };
          Object.assign(globalThis, __require("stream/web"));
          process2.emitWarning = emitWarning;
        } catch (error) {
          process2.emitWarning = emitWarning;
          throw error;
        }
      } catch (error) {
        Object.assign(globalThis, require_ponyfill_es2018());
      }
    }
    try {
      const { Blob: Blob3 } = __require("buffer");
      if (Blob3 && !Blob3.prototype.stream) {
        Blob3.prototype.stream = function name(params) {
          let position = 0;
          const blob = this;
          return new ReadableStream({
            type: "bytes",
            async pull(ctrl) {
              const chunk = blob.slice(position, Math.min(blob.size, position + POOL_SIZE2));
              const buffer = await chunk.arrayBuffer();
              position += buffer.byteLength;
              ctrl.enqueue(new Uint8Array(buffer));
              if (position === blob.size) {
                ctrl.close();
              }
            }
          });
        };
      }
    } catch (error) {
    }
  }
});

// node_modules/fetch-blob/index.js
async function* toIterator(parts, clone2 = true) {
  for (const part of parts) {
    if ("stream" in part) {
      yield* (
        /** @type {AsyncIterableIterator<Uint8Array>} */
        part.stream()
      );
    } else if (ArrayBuffer.isView(part)) {
      if (clone2) {
        let position = part.byteOffset;
        const end = part.byteOffset + part.byteLength;
        while (position !== end) {
          const size = Math.min(end - position, POOL_SIZE);
          const chunk = part.buffer.slice(position, position + size);
          position += chunk.byteLength;
          yield new Uint8Array(chunk);
        }
      } else {
        yield part;
      }
    } else {
      let position = 0, b = (
        /** @type {Blob} */
        part
      );
      while (position !== b.size) {
        const chunk = b.slice(position, Math.min(b.size, position + POOL_SIZE));
        const buffer = await chunk.arrayBuffer();
        position += buffer.byteLength;
        yield new Uint8Array(buffer);
      }
    }
  }
}
var POOL_SIZE, _Blob, Blob2, fetch_blob_default;
var init_fetch_blob = __esm({
  "node_modules/fetch-blob/index.js"() {
    __toESM(require_streams(), 1);
    POOL_SIZE = 65536;
    _Blob = class Blob {
      /** @type {Array.<(Blob|Uint8Array)>} */
      #parts = [];
      #type = "";
      #size = 0;
      #endings = "transparent";
      /**
       * The Blob() constructor returns a new Blob object. The content
       * of the blob consists of the concatenation of the values given
       * in the parameter array.
       *
       * @param {*} blobParts
       * @param {{ type?: string, endings?: string }} [options]
       */
      constructor(blobParts = [], options = {}) {
        if (typeof blobParts !== "object" || blobParts === null) {
          throw new TypeError("Failed to construct 'Blob': The provided value cannot be converted to a sequence.");
        }
        if (typeof blobParts[Symbol.iterator] !== "function") {
          throw new TypeError("Failed to construct 'Blob': The object must have a callable @@iterator property.");
        }
        if (typeof options !== "object" && typeof options !== "function") {
          throw new TypeError("Failed to construct 'Blob': parameter 2 cannot convert to dictionary.");
        }
        if (options === null)
          options = {};
        const encoder = new TextEncoder();
        for (const element of blobParts) {
          let part;
          if (ArrayBuffer.isView(element)) {
            part = new Uint8Array(element.buffer.slice(element.byteOffset, element.byteOffset + element.byteLength));
          } else if (element instanceof ArrayBuffer) {
            part = new Uint8Array(element.slice(0));
          } else if (element instanceof Blob) {
            part = element;
          } else {
            part = encoder.encode(`${element}`);
          }
          this.#size += ArrayBuffer.isView(part) ? part.byteLength : part.size;
          this.#parts.push(part);
        }
        this.#endings = `${options.endings === void 0 ? "transparent" : options.endings}`;
        const type = options.type === void 0 ? "" : String(options.type);
        this.#type = /^[\x20-\x7E]*$/.test(type) ? type : "";
      }
      /**
       * The Blob interface's size property returns the
       * size of the Blob in bytes.
       */
      get size() {
        return this.#size;
      }
      /**
       * The type property of a Blob object returns the MIME type of the file.
       */
      get type() {
        return this.#type;
      }
      /**
       * The text() method in the Blob interface returns a Promise
       * that resolves with a string containing the contents of
       * the blob, interpreted as UTF-8.
       *
       * @return {Promise<string>}
       */
      async text() {
        const decoder = new TextDecoder();
        let str = "";
        for await (const part of toIterator(this.#parts, false)) {
          str += decoder.decode(part, { stream: true });
        }
        str += decoder.decode();
        return str;
      }
      /**
       * The arrayBuffer() method in the Blob interface returns a
       * Promise that resolves with the contents of the blob as
       * binary data contained in an ArrayBuffer.
       *
       * @return {Promise<ArrayBuffer>}
       */
      async arrayBuffer() {
        const data = new Uint8Array(this.size);
        let offset = 0;
        for await (const chunk of toIterator(this.#parts, false)) {
          data.set(chunk, offset);
          offset += chunk.length;
        }
        return data.buffer;
      }
      stream() {
        const it = toIterator(this.#parts, true);
        return new globalThis.ReadableStream({
          // @ts-ignore
          type: "bytes",
          async pull(ctrl) {
            const chunk = await it.next();
            chunk.done ? ctrl.close() : ctrl.enqueue(chunk.value);
          },
          async cancel() {
            await it.return();
          }
        });
      }
      /**
       * The Blob interface's slice() method creates and returns a
       * new Blob object which contains data from a subset of the
       * blob on which it's called.
       *
       * @param {number} [start]
       * @param {number} [end]
       * @param {string} [type]
       */
      slice(start = 0, end = this.size, type = "") {
        const { size } = this;
        let relativeStart = start < 0 ? Math.max(size + start, 0) : Math.min(start, size);
        let relativeEnd = end < 0 ? Math.max(size + end, 0) : Math.min(end, size);
        const span = Math.max(relativeEnd - relativeStart, 0);
        const parts = this.#parts;
        const blobParts = [];
        let added = 0;
        for (const part of parts) {
          if (added >= span) {
            break;
          }
          const size2 = ArrayBuffer.isView(part) ? part.byteLength : part.size;
          if (relativeStart && size2 <= relativeStart) {
            relativeStart -= size2;
            relativeEnd -= size2;
          } else {
            let chunk;
            if (ArrayBuffer.isView(part)) {
              chunk = part.subarray(relativeStart, Math.min(size2, relativeEnd));
              added += chunk.byteLength;
            } else {
              chunk = part.slice(relativeStart, Math.min(size2, relativeEnd));
              added += chunk.size;
            }
            relativeEnd -= size2;
            blobParts.push(chunk);
            relativeStart = 0;
          }
        }
        const blob = new Blob([], { type: String(type).toLowerCase() });
        blob.#size = span;
        blob.#parts = blobParts;
        return blob;
      }
      get [Symbol.toStringTag]() {
        return "Blob";
      }
      static [Symbol.hasInstance](object) {
        return object && typeof object === "object" && typeof object.constructor === "function" && (typeof object.stream === "function" || typeof object.arrayBuffer === "function") && /^(Blob|File)$/.test(object[Symbol.toStringTag]);
      }
    };
    Object.defineProperties(_Blob.prototype, {
      size: { enumerable: true },
      type: { enumerable: true },
      slice: { enumerable: true }
    });
    Blob2 = _Blob;
    fetch_blob_default = Blob2;
  }
});

// node_modules/fetch-blob/file.js
var _File, File2, file_default;
var init_file = __esm({
  "node_modules/fetch-blob/file.js"() {
    init_fetch_blob();
    _File = class File extends fetch_blob_default {
      #lastModified = 0;
      #name = "";
      /**
       * @param {*[]} fileBits
       * @param {string} fileName
       * @param {{lastModified?: number, type?: string}} options
       */
      // @ts-ignore
      constructor(fileBits, fileName, options = {}) {
        if (arguments.length < 2) {
          throw new TypeError(`Failed to construct 'File': 2 arguments required, but only ${arguments.length} present.`);
        }
        super(fileBits, options);
        if (options === null)
          options = {};
        const lastModified = options.lastModified === void 0 ? Date.now() : Number(options.lastModified);
        if (!Number.isNaN(lastModified)) {
          this.#lastModified = lastModified;
        }
        this.#name = String(fileName);
      }
      get name() {
        return this.#name;
      }
      get lastModified() {
        return this.#lastModified;
      }
      get [Symbol.toStringTag]() {
        return "File";
      }
      static [Symbol.hasInstance](object) {
        return !!object && object instanceof fetch_blob_default && /^(File)$/.test(object[Symbol.toStringTag]);
      }
    };
    File2 = _File;
    file_default = File2;
  }
});

// node_modules/formdata-polyfill/esm.min.js
function formDataToBlob(F2, B = fetch_blob_default) {
  var b = `${r()}${r()}`.replace(/\./g, "").slice(-28).padStart(32, "-"), c = [], p = `--${b}\r
Content-Disposition: form-data; name="`;
  F2.forEach((v, n) => typeof v == "string" ? c.push(p + e(n) + `"\r
\r
${v.replace(/\r(?!\n)|(?<!\r)\n/g, "\r\n")}\r
`) : c.push(p + e(n) + `"; filename="${e(v.name, 1)}"\r
Content-Type: ${v.type || "application/octet-stream"}\r
\r
`, v, "\r\n"));
  c.push(`--${b}--`);
  return new B(c, { type: "multipart/form-data; boundary=" + b });
}
var t, i, h, r, m, f, e, x, FormData;
var init_esm_min = __esm({
  "node_modules/formdata-polyfill/esm.min.js"() {
    init_fetch_blob();
    init_file();
    ({ toStringTag: t, iterator: i, hasInstance: h } = Symbol);
    r = Math.random;
    m = "append,set,get,getAll,delete,keys,values,entries,forEach,constructor".split(",");
    f = (a, b, c) => (a += "", /^(Blob|File)$/.test(b && b[t]) ? [(c = c !== void 0 ? c + "" : b[t] == "File" ? b.name : "blob", a), b.name !== c || b[t] == "blob" ? new file_default([b], c, b) : b] : [a, b + ""]);
    e = (c, f3) => (f3 ? c : c.replace(/\r?\n|\r/g, "\r\n")).replace(/\n/g, "%0A").replace(/\r/g, "%0D").replace(/"/g, "%22");
    x = (n, a, e2) => {
      if (a.length < e2) {
        throw new TypeError(`Failed to execute '${n}' on 'FormData': ${e2} arguments required, but only ${a.length} present.`);
      }
    };
    FormData = class FormData2 {
      #d = [];
      constructor(...a) {
        if (a.length)
          throw new TypeError(`Failed to construct 'FormData': parameter 1 is not of type 'HTMLFormElement'.`);
      }
      get [t]() {
        return "FormData";
      }
      [i]() {
        return this.entries();
      }
      static [h](o) {
        return o && typeof o === "object" && o[t] === "FormData" && !m.some((m2) => typeof o[m2] != "function");
      }
      append(...a) {
        x("append", arguments, 2);
        this.#d.push(f(...a));
      }
      delete(a) {
        x("delete", arguments, 1);
        a += "";
        this.#d = this.#d.filter(([b]) => b !== a);
      }
      get(a) {
        x("get", arguments, 1);
        a += "";
        for (var b = this.#d, l = b.length, c = 0; c < l; c++)
          if (b[c][0] === a)
            return b[c][1];
        return null;
      }
      getAll(a, b) {
        x("getAll", arguments, 1);
        b = [];
        a += "";
        this.#d.forEach((c) => c[0] === a && b.push(c[1]));
        return b;
      }
      has(a) {
        x("has", arguments, 1);
        a += "";
        return this.#d.some((b) => b[0] === a);
      }
      forEach(a, b) {
        x("forEach", arguments, 1);
        for (var [c, d] of this)
          a.call(b, d, c, this);
      }
      set(...a) {
        x("set", arguments, 2);
        var b = [], c = true;
        a = f(...a);
        this.#d.forEach((d) => {
          d[0] === a[0] ? c && (c = !b.push(a)) : b.push(d);
        });
        c && b.push(a);
        this.#d = b;
      }
      *entries() {
        yield* this.#d;
      }
      *keys() {
        for (var [a] of this)
          yield a;
      }
      *values() {
        for (var [, a] of this)
          yield a;
      }
    };
  }
});

// node_modules/node-fetch/src/errors/base.js
var FetchBaseError;
var init_base = __esm({
  "node_modules/node-fetch/src/errors/base.js"() {
    FetchBaseError = class extends Error {
      constructor(message, type) {
        super(message);
        Error.captureStackTrace(this, this.constructor);
        this.type = type;
      }
      get name() {
        return this.constructor.name;
      }
      get [Symbol.toStringTag]() {
        return this.constructor.name;
      }
    };
  }
});

// node_modules/node-fetch/src/errors/fetch-error.js
var FetchError;
var init_fetch_error = __esm({
  "node_modules/node-fetch/src/errors/fetch-error.js"() {
    init_base();
    FetchError = class extends FetchBaseError {
      /**
       * @param  {string} message -      Error message for human
       * @param  {string} [type] -        Error type for machine
       * @param  {SystemError} [systemError] - For Node.js system error
       */
      constructor(message, type, systemError) {
        super(message, type);
        if (systemError) {
          this.code = this.errno = systemError.code;
          this.erroredSysCall = systemError.syscall;
        }
      }
    };
  }
});

// node_modules/node-fetch/src/utils/is.js
var NAME, isURLSearchParameters, isBlob, isAbortSignal, isDomainOrSubdomain, isSameProtocol;
var init_is = __esm({
  "node_modules/node-fetch/src/utils/is.js"() {
    NAME = Symbol.toStringTag;
    isURLSearchParameters = (object) => {
      return typeof object === "object" && typeof object.append === "function" && typeof object.delete === "function" && typeof object.get === "function" && typeof object.getAll === "function" && typeof object.has === "function" && typeof object.set === "function" && typeof object.sort === "function" && object[NAME] === "URLSearchParams";
    };
    isBlob = (object) => {
      return object && typeof object === "object" && typeof object.arrayBuffer === "function" && typeof object.type === "string" && typeof object.stream === "function" && typeof object.constructor === "function" && /^(Blob|File)$/.test(object[NAME]);
    };
    isAbortSignal = (object) => {
      return typeof object === "object" && (object[NAME] === "AbortSignal" || object[NAME] === "EventTarget");
    };
    isDomainOrSubdomain = (destination, original) => {
      const orig = new URL(original).hostname;
      const dest = new URL(destination).hostname;
      return orig === dest || orig.endsWith(`.${dest}`);
    };
    isSameProtocol = (destination, original) => {
      const orig = new URL(original).protocol;
      const dest = new URL(destination).protocol;
      return orig === dest;
    };
  }
});

// node_modules/node-domexception/index.js
var require_node_domexception = __commonJS({
  "node_modules/node-domexception/index.js"(exports, module) {
    if (!globalThis.DOMException) {
      try {
        const { MessageChannel } = __require("worker_threads"), port = new MessageChannel().port1, ab = new ArrayBuffer();
        port.postMessage(ab, [ab, ab]);
      } catch (err) {
        err.constructor.name === "DOMException" && (globalThis.DOMException = err.constructor);
      }
    }
    module.exports = globalThis.DOMException;
  }
});
var import_node_domexception, stat, blobFromSync, blobFrom, fileFrom, fileFromSync, fromBlob, fromFile, BlobDataItem;
var init_from = __esm({
  "node_modules/fetch-blob/from.js"() {
    import_node_domexception = __toESM(require_node_domexception(), 1);
    init_file();
    init_fetch_blob();
    ({ stat } = promises);
    blobFromSync = (path, type) => fromBlob(statSync(path), path, type);
    blobFrom = (path, type) => stat(path).then((stat2) => fromBlob(stat2, path, type));
    fileFrom = (path, type) => stat(path).then((stat2) => fromFile(stat2, path, type));
    fileFromSync = (path, type) => fromFile(statSync(path), path, type);
    fromBlob = (stat2, path, type = "") => new fetch_blob_default([new BlobDataItem({
      path,
      size: stat2.size,
      lastModified: stat2.mtimeMs,
      start: 0
    })], { type });
    fromFile = (stat2, path, type = "") => new file_default([new BlobDataItem({
      path,
      size: stat2.size,
      lastModified: stat2.mtimeMs,
      start: 0
    })], basename(path), { type, lastModified: stat2.mtimeMs });
    BlobDataItem = class _BlobDataItem {
      #path;
      #start;
      constructor(options) {
        this.#path = options.path;
        this.#start = options.start;
        this.size = options.size;
        this.lastModified = options.lastModified;
      }
      /**
       * Slicing arguments is first validated and formatted
       * to not be out of range by Blob.prototype.slice
       */
      slice(start, end) {
        return new _BlobDataItem({
          path: this.#path,
          lastModified: this.lastModified,
          size: end - start,
          start: this.#start + start
        });
      }
      async *stream() {
        const { mtimeMs } = await stat(this.#path);
        if (mtimeMs > this.lastModified) {
          throw new import_node_domexception.default("The requested file could not be read, typically due to permission problems that have occurred after a reference to a file was acquired.", "NotReadableError");
        }
        yield* createReadStream(this.#path, {
          start: this.#start,
          end: this.#start + this.size - 1
        });
      }
      get [Symbol.toStringTag]() {
        return "Blob";
      }
    };
  }
});

// node_modules/node-fetch/src/utils/multipart-parser.js
var multipart_parser_exports = {};
__export(multipart_parser_exports, {
  toFormData: () => toFormData
});
function _fileName(headerValue) {
  const m2 = headerValue.match(/\bfilename=("(.*?)"|([^()<>@,;:\\"/[\]?={}\s\t]+))($|;\s)/i);
  if (!m2) {
    return;
  }
  const match = m2[2] || m2[3] || "";
  let filename = match.slice(match.lastIndexOf("\\") + 1);
  filename = filename.replace(/%22/g, '"');
  filename = filename.replace(/&#(\d{4});/g, (m3, code) => {
    return String.fromCharCode(code);
  });
  return filename;
}
async function toFormData(Body2, ct) {
  if (!/multipart/i.test(ct)) {
    throw new TypeError("Failed to fetch");
  }
  const m2 = ct.match(/boundary=(?:"([^"]+)"|([^;]+))/i);
  if (!m2) {
    throw new TypeError("no or bad content-type header, no multipart boundary");
  }
  const parser = new MultipartParser(m2[1] || m2[2]);
  let headerField;
  let headerValue;
  let entryValue;
  let entryName;
  let contentType;
  let filename;
  const entryChunks = [];
  const formData = new FormData();
  const onPartData = (ui8a) => {
    entryValue += decoder.decode(ui8a, { stream: true });
  };
  const appendToFile = (ui8a) => {
    entryChunks.push(ui8a);
  };
  const appendFileToFormData = () => {
    const file = new file_default(entryChunks, filename, { type: contentType });
    formData.append(entryName, file);
  };
  const appendEntryToFormData = () => {
    formData.append(entryName, entryValue);
  };
  const decoder = new TextDecoder("utf-8");
  decoder.decode();
  parser.onPartBegin = function() {
    parser.onPartData = onPartData;
    parser.onPartEnd = appendEntryToFormData;
    headerField = "";
    headerValue = "";
    entryValue = "";
    entryName = "";
    contentType = "";
    filename = null;
    entryChunks.length = 0;
  };
  parser.onHeaderField = function(ui8a) {
    headerField += decoder.decode(ui8a, { stream: true });
  };
  parser.onHeaderValue = function(ui8a) {
    headerValue += decoder.decode(ui8a, { stream: true });
  };
  parser.onHeaderEnd = function() {
    headerValue += decoder.decode();
    headerField = headerField.toLowerCase();
    if (headerField === "content-disposition") {
      const m3 = headerValue.match(/\bname=("([^"]*)"|([^()<>@,;:\\"/[\]?={}\s\t]+))/i);
      if (m3) {
        entryName = m3[2] || m3[3] || "";
      }
      filename = _fileName(headerValue);
      if (filename) {
        parser.onPartData = appendToFile;
        parser.onPartEnd = appendFileToFormData;
      }
    } else if (headerField === "content-type") {
      contentType = headerValue;
    }
    headerValue = "";
    headerField = "";
  };
  for await (const chunk of Body2) {
    parser.write(chunk);
  }
  parser.end();
  return formData;
}
var s, S, f2, F, LF, CR, SPACE, HYPHEN, COLON, A, Z, lower, noop, MultipartParser;
var init_multipart_parser = __esm({
  "node_modules/node-fetch/src/utils/multipart-parser.js"() {
    init_from();
    init_esm_min();
    s = 0;
    S = {
      START_BOUNDARY: s++,
      HEADER_FIELD_START: s++,
      HEADER_FIELD: s++,
      HEADER_VALUE_START: s++,
      HEADER_VALUE: s++,
      HEADER_VALUE_ALMOST_DONE: s++,
      HEADERS_ALMOST_DONE: s++,
      PART_DATA_START: s++,
      PART_DATA: s++,
      END: s++
    };
    f2 = 1;
    F = {
      PART_BOUNDARY: f2,
      LAST_BOUNDARY: f2 *= 2
    };
    LF = 10;
    CR = 13;
    SPACE = 32;
    HYPHEN = 45;
    COLON = 58;
    A = 97;
    Z = 122;
    lower = (c) => c | 32;
    noop = () => {
    };
    MultipartParser = class {
      /**
       * @param {string} boundary
       */
      constructor(boundary) {
        this.index = 0;
        this.flags = 0;
        this.onHeaderEnd = noop;
        this.onHeaderField = noop;
        this.onHeadersEnd = noop;
        this.onHeaderValue = noop;
        this.onPartBegin = noop;
        this.onPartData = noop;
        this.onPartEnd = noop;
        this.boundaryChars = {};
        boundary = "\r\n--" + boundary;
        const ui8a = new Uint8Array(boundary.length);
        for (let i2 = 0; i2 < boundary.length; i2++) {
          ui8a[i2] = boundary.charCodeAt(i2);
          this.boundaryChars[ui8a[i2]] = true;
        }
        this.boundary = ui8a;
        this.lookbehind = new Uint8Array(this.boundary.length + 8);
        this.state = S.START_BOUNDARY;
      }
      /**
       * @param {Uint8Array} data
       */
      write(data) {
        let i2 = 0;
        const length_ = data.length;
        let previousIndex = this.index;
        let { lookbehind, boundary, boundaryChars, index, state, flags } = this;
        const boundaryLength = this.boundary.length;
        const boundaryEnd = boundaryLength - 1;
        const bufferLength = data.length;
        let c;
        let cl;
        const mark = (name) => {
          this[name + "Mark"] = i2;
        };
        const clear = (name) => {
          delete this[name + "Mark"];
        };
        const callback = (callbackSymbol, start, end, ui8a) => {
          if (start === void 0 || start !== end) {
            this[callbackSymbol](ui8a && ui8a.subarray(start, end));
          }
        };
        const dataCallback = (name, clear2) => {
          const markSymbol = name + "Mark";
          if (!(markSymbol in this)) {
            return;
          }
          if (clear2) {
            callback(name, this[markSymbol], i2, data);
            delete this[markSymbol];
          } else {
            callback(name, this[markSymbol], data.length, data);
            this[markSymbol] = 0;
          }
        };
        for (i2 = 0; i2 < length_; i2++) {
          c = data[i2];
          switch (state) {
            case S.START_BOUNDARY:
              if (index === boundary.length - 2) {
                if (c === HYPHEN) {
                  flags |= F.LAST_BOUNDARY;
                } else if (c !== CR) {
                  return;
                }
                index++;
                break;
              } else if (index - 1 === boundary.length - 2) {
                if (flags & F.LAST_BOUNDARY && c === HYPHEN) {
                  state = S.END;
                  flags = 0;
                } else if (!(flags & F.LAST_BOUNDARY) && c === LF) {
                  index = 0;
                  callback("onPartBegin");
                  state = S.HEADER_FIELD_START;
                } else {
                  return;
                }
                break;
              }
              if (c !== boundary[index + 2]) {
                index = -2;
              }
              if (c === boundary[index + 2]) {
                index++;
              }
              break;
            case S.HEADER_FIELD_START:
              state = S.HEADER_FIELD;
              mark("onHeaderField");
              index = 0;
            case S.HEADER_FIELD:
              if (c === CR) {
                clear("onHeaderField");
                state = S.HEADERS_ALMOST_DONE;
                break;
              }
              index++;
              if (c === HYPHEN) {
                break;
              }
              if (c === COLON) {
                if (index === 1) {
                  return;
                }
                dataCallback("onHeaderField", true);
                state = S.HEADER_VALUE_START;
                break;
              }
              cl = lower(c);
              if (cl < A || cl > Z) {
                return;
              }
              break;
            case S.HEADER_VALUE_START:
              if (c === SPACE) {
                break;
              }
              mark("onHeaderValue");
              state = S.HEADER_VALUE;
            case S.HEADER_VALUE:
              if (c === CR) {
                dataCallback("onHeaderValue", true);
                callback("onHeaderEnd");
                state = S.HEADER_VALUE_ALMOST_DONE;
              }
              break;
            case S.HEADER_VALUE_ALMOST_DONE:
              if (c !== LF) {
                return;
              }
              state = S.HEADER_FIELD_START;
              break;
            case S.HEADERS_ALMOST_DONE:
              if (c !== LF) {
                return;
              }
              callback("onHeadersEnd");
              state = S.PART_DATA_START;
              break;
            case S.PART_DATA_START:
              state = S.PART_DATA;
              mark("onPartData");
            case S.PART_DATA:
              previousIndex = index;
              if (index === 0) {
                i2 += boundaryEnd;
                while (i2 < bufferLength && !(data[i2] in boundaryChars)) {
                  i2 += boundaryLength;
                }
                i2 -= boundaryEnd;
                c = data[i2];
              }
              if (index < boundary.length) {
                if (boundary[index] === c) {
                  if (index === 0) {
                    dataCallback("onPartData", true);
                  }
                  index++;
                } else {
                  index = 0;
                }
              } else if (index === boundary.length) {
                index++;
                if (c === CR) {
                  flags |= F.PART_BOUNDARY;
                } else if (c === HYPHEN) {
                  flags |= F.LAST_BOUNDARY;
                } else {
                  index = 0;
                }
              } else if (index - 1 === boundary.length) {
                if (flags & F.PART_BOUNDARY) {
                  index = 0;
                  if (c === LF) {
                    flags &= ~F.PART_BOUNDARY;
                    callback("onPartEnd");
                    callback("onPartBegin");
                    state = S.HEADER_FIELD_START;
                    break;
                  }
                } else if (flags & F.LAST_BOUNDARY) {
                  if (c === HYPHEN) {
                    callback("onPartEnd");
                    state = S.END;
                    flags = 0;
                  } else {
                    index = 0;
                  }
                } else {
                  index = 0;
                }
              }
              if (index > 0) {
                lookbehind[index - 1] = c;
              } else if (previousIndex > 0) {
                const _lookbehind = new Uint8Array(lookbehind.buffer, lookbehind.byteOffset, lookbehind.byteLength);
                callback("onPartData", 0, previousIndex, _lookbehind);
                previousIndex = 0;
                mark("onPartData");
                i2--;
              }
              break;
            case S.END:
              break;
            default:
              throw new Error(`Unexpected state entered: ${state}`);
          }
        }
        dataCallback("onHeaderField");
        dataCallback("onHeaderValue");
        dataCallback("onPartData");
        this.index = index;
        this.state = state;
        this.flags = flags;
      }
      end() {
        if (this.state === S.HEADER_FIELD_START && this.index === 0 || this.state === S.PART_DATA && this.index === this.boundary.length) {
          this.onPartEnd();
        } else if (this.state !== S.END) {
          throw new Error("MultipartParser.end(): stream ended unexpectedly");
        }
      }
    };
  }
});
async function consumeBody(data) {
  if (data[INTERNALS].disturbed) {
    throw new TypeError(`body used already for: ${data.url}`);
  }
  data[INTERNALS].disturbed = true;
  if (data[INTERNALS].error) {
    throw data[INTERNALS].error;
  }
  const { body } = data;
  if (body === null) {
    return Buffer$1.alloc(0);
  }
  if (!(body instanceof Stream)) {
    return Buffer$1.alloc(0);
  }
  const accum = [];
  let accumBytes = 0;
  try {
    for await (const chunk of body) {
      if (data.size > 0 && accumBytes + chunk.length > data.size) {
        const error = new FetchError(`content size at ${data.url} over limit: ${data.size}`, "max-size");
        body.destroy(error);
        throw error;
      }
      accumBytes += chunk.length;
      accum.push(chunk);
    }
  } catch (error) {
    const error_ = error instanceof FetchBaseError ? error : new FetchError(`Invalid response body while trying to fetch ${data.url}: ${error.message}`, "system", error);
    throw error_;
  }
  if (body.readableEnded === true || body._readableState.ended === true) {
    try {
      if (accum.every((c) => typeof c === "string")) {
        return Buffer$1.from(accum.join(""));
      }
      return Buffer$1.concat(accum, accumBytes);
    } catch (error) {
      throw new FetchError(`Could not create Buffer from response body for ${data.url}: ${error.message}`, "system", error);
    }
  } else {
    throw new FetchError(`Premature close of server response while trying to fetch ${data.url}`);
  }
}
var pipeline, INTERNALS, Body, clone, getNonSpecFormDataBoundary, extractContentType, getTotalBytes, writeToStream;
var init_body = __esm({
  "node_modules/node-fetch/src/body.js"() {
    init_fetch_blob();
    init_esm_min();
    init_fetch_error();
    init_base();
    init_is();
    pipeline = promisify(Stream.pipeline);
    INTERNALS = Symbol("Body internals");
    Body = class {
      constructor(body, {
        size = 0
      } = {}) {
        let boundary = null;
        if (body === null) {
          body = null;
        } else if (isURLSearchParameters(body)) {
          body = Buffer$1.from(body.toString());
        } else if (isBlob(body)) ; else if (Buffer$1.isBuffer(body)) ; else if (types.isAnyArrayBuffer(body)) {
          body = Buffer$1.from(body);
        } else if (ArrayBuffer.isView(body)) {
          body = Buffer$1.from(body.buffer, body.byteOffset, body.byteLength);
        } else if (body instanceof Stream) ; else if (body instanceof FormData) {
          body = formDataToBlob(body);
          boundary = body.type.split("=")[1];
        } else {
          body = Buffer$1.from(String(body));
        }
        let stream = body;
        if (Buffer$1.isBuffer(body)) {
          stream = Stream.Readable.from(body);
        } else if (isBlob(body)) {
          stream = Stream.Readable.from(body.stream());
        }
        this[INTERNALS] = {
          body,
          stream,
          boundary,
          disturbed: false,
          error: null
        };
        this.size = size;
        if (body instanceof Stream) {
          body.on("error", (error_) => {
            const error = error_ instanceof FetchBaseError ? error_ : new FetchError(`Invalid response body while trying to fetch ${this.url}: ${error_.message}`, "system", error_);
            this[INTERNALS].error = error;
          });
        }
      }
      get body() {
        return this[INTERNALS].stream;
      }
      get bodyUsed() {
        return this[INTERNALS].disturbed;
      }
      /**
       * Decode response as ArrayBuffer
       *
       * @return  Promise
       */
      async arrayBuffer() {
        const { buffer, byteOffset, byteLength } = await consumeBody(this);
        return buffer.slice(byteOffset, byteOffset + byteLength);
      }
      async formData() {
        const ct = this.headers.get("content-type");
        if (ct.startsWith("application/x-www-form-urlencoded")) {
          const formData = new FormData();
          const parameters = new URLSearchParams(await this.text());
          for (const [name, value] of parameters) {
            formData.append(name, value);
          }
          return formData;
        }
        const { toFormData: toFormData2 } = await Promise.resolve().then(() => (init_multipart_parser(), multipart_parser_exports));
        return toFormData2(this.body, ct);
      }
      /**
       * Return raw response as Blob
       *
       * @return Promise
       */
      async blob() {
        const ct = this.headers && this.headers.get("content-type") || this[INTERNALS].body && this[INTERNALS].body.type || "";
        const buf = await this.arrayBuffer();
        return new fetch_blob_default([buf], {
          type: ct
        });
      }
      /**
       * Decode response as json
       *
       * @return  Promise
       */
      async json() {
        const text = await this.text();
        return JSON.parse(text);
      }
      /**
       * Decode response as text
       *
       * @return  Promise
       */
      async text() {
        const buffer = await consumeBody(this);
        return new TextDecoder().decode(buffer);
      }
      /**
       * Decode response as buffer (non-spec api)
       *
       * @return  Promise
       */
      buffer() {
        return consumeBody(this);
      }
    };
    Body.prototype.buffer = deprecate(Body.prototype.buffer, "Please use 'response.arrayBuffer()' instead of 'response.buffer()'", "node-fetch#buffer");
    Object.defineProperties(Body.prototype, {
      body: { enumerable: true },
      bodyUsed: { enumerable: true },
      arrayBuffer: { enumerable: true },
      blob: { enumerable: true },
      json: { enumerable: true },
      text: { enumerable: true },
      data: { get: deprecate(
        () => {
        },
        "data doesn't exist, use json(), text(), arrayBuffer(), or body instead",
        "https://github.com/node-fetch/node-fetch/issues/1000 (response)"
      ) }
    });
    clone = (instance, highWaterMark) => {
      let p1;
      let p2;
      let { body } = instance[INTERNALS];
      if (instance.bodyUsed) {
        throw new Error("cannot clone body after it is used");
      }
      if (body instanceof Stream && typeof body.getBoundary !== "function") {
        p1 = new PassThrough({ highWaterMark });
        p2 = new PassThrough({ highWaterMark });
        body.pipe(p1);
        body.pipe(p2);
        instance[INTERNALS].stream = p1;
        body = p2;
      }
      return body;
    };
    getNonSpecFormDataBoundary = deprecate(
      (body) => body.getBoundary(),
      "form-data doesn't follow the spec and requires special treatment. Use alternative package",
      "https://github.com/node-fetch/node-fetch/issues/1167"
    );
    extractContentType = (body, request) => {
      if (body === null) {
        return null;
      }
      if (typeof body === "string") {
        return "text/plain;charset=UTF-8";
      }
      if (isURLSearchParameters(body)) {
        return "application/x-www-form-urlencoded;charset=UTF-8";
      }
      if (isBlob(body)) {
        return body.type || null;
      }
      if (Buffer$1.isBuffer(body) || types.isAnyArrayBuffer(body) || ArrayBuffer.isView(body)) {
        return null;
      }
      if (body instanceof FormData) {
        return `multipart/form-data; boundary=${request[INTERNALS].boundary}`;
      }
      if (body && typeof body.getBoundary === "function") {
        return `multipart/form-data;boundary=${getNonSpecFormDataBoundary(body)}`;
      }
      if (body instanceof Stream) {
        return null;
      }
      return "text/plain;charset=UTF-8";
    };
    getTotalBytes = (request) => {
      const { body } = request[INTERNALS];
      if (body === null) {
        return 0;
      }
      if (isBlob(body)) {
        return body.size;
      }
      if (Buffer$1.isBuffer(body)) {
        return body.length;
      }
      if (body && typeof body.getLengthSync === "function") {
        return body.hasKnownLength && body.hasKnownLength() ? body.getLengthSync() : null;
      }
      return null;
    };
    writeToStream = async (dest, { body }) => {
      if (body === null) {
        dest.end();
      } else {
        await pipeline(body, dest);
      }
    };
  }
});
function fromRawHeaders(headers = []) {
  return new Headers2(
    headers.reduce((result, value, index, array) => {
      if (index % 2 === 0) {
        result.push(array.slice(index, index + 2));
      }
      return result;
    }, []).filter(([name, value]) => {
      try {
        validateHeaderName(name);
        validateHeaderValue(name, String(value));
        return true;
      } catch {
        return false;
      }
    })
  );
}
var validateHeaderName, validateHeaderValue, Headers2;
var init_headers = __esm({
  "node_modules/node-fetch/src/headers.js"() {
    validateHeaderName = typeof http.validateHeaderName === "function" ? http.validateHeaderName : (name) => {
      if (!/^[\^`\-\w!#$%&'*+.|~]+$/.test(name)) {
        const error = new TypeError(`Header name must be a valid HTTP token [${name}]`);
        Object.defineProperty(error, "code", { value: "ERR_INVALID_HTTP_TOKEN" });
        throw error;
      }
    };
    validateHeaderValue = typeof http.validateHeaderValue === "function" ? http.validateHeaderValue : (name, value) => {
      if (/[^\t\u0020-\u007E\u0080-\u00FF]/.test(value)) {
        const error = new TypeError(`Invalid character in header content ["${name}"]`);
        Object.defineProperty(error, "code", { value: "ERR_INVALID_CHAR" });
        throw error;
      }
    };
    Headers2 = class _Headers extends URLSearchParams {
      /**
       * Headers class
       *
       * @constructor
       * @param {HeadersInit} [init] - Response headers
       */
      constructor(init) {
        let result = [];
        if (init instanceof _Headers) {
          const raw = init.raw();
          for (const [name, values] of Object.entries(raw)) {
            result.push(...values.map((value) => [name, value]));
          }
        } else if (init == null) ; else if (typeof init === "object" && !types.isBoxedPrimitive(init)) {
          const method = init[Symbol.iterator];
          if (method == null) {
            result.push(...Object.entries(init));
          } else {
            if (typeof method !== "function") {
              throw new TypeError("Header pairs must be iterable");
            }
            result = [...init].map((pair) => {
              if (typeof pair !== "object" || types.isBoxedPrimitive(pair)) {
                throw new TypeError("Each header pair must be an iterable object");
              }
              return [...pair];
            }).map((pair) => {
              if (pair.length !== 2) {
                throw new TypeError("Each header pair must be a name/value tuple");
              }
              return [...pair];
            });
          }
        } else {
          throw new TypeError("Failed to construct 'Headers': The provided value is not of type '(sequence<sequence<ByteString>> or record<ByteString, ByteString>)");
        }
        result = result.length > 0 ? result.map(([name, value]) => {
          validateHeaderName(name);
          validateHeaderValue(name, String(value));
          return [String(name).toLowerCase(), String(value)];
        }) : void 0;
        super(result);
        return new Proxy(this, {
          get(target, p, receiver) {
            switch (p) {
              case "append":
              case "set":
                return (name, value) => {
                  validateHeaderName(name);
                  validateHeaderValue(name, String(value));
                  return URLSearchParams.prototype[p].call(
                    target,
                    String(name).toLowerCase(),
                    String(value)
                  );
                };
              case "delete":
              case "has":
              case "getAll":
                return (name) => {
                  validateHeaderName(name);
                  return URLSearchParams.prototype[p].call(
                    target,
                    String(name).toLowerCase()
                  );
                };
              case "keys":
                return () => {
                  target.sort();
                  return new Set(URLSearchParams.prototype.keys.call(target)).keys();
                };
              default:
                return Reflect.get(target, p, receiver);
            }
          }
        });
      }
      get [Symbol.toStringTag]() {
        return this.constructor.name;
      }
      toString() {
        return Object.prototype.toString.call(this);
      }
      get(name) {
        const values = this.getAll(name);
        if (values.length === 0) {
          return null;
        }
        let value = values.join(", ");
        if (/^content-encoding$/i.test(name)) {
          value = value.toLowerCase();
        }
        return value;
      }
      forEach(callback, thisArg = void 0) {
        for (const name of this.keys()) {
          Reflect.apply(callback, thisArg, [this.get(name), name, this]);
        }
      }
      *values() {
        for (const name of this.keys()) {
          yield this.get(name);
        }
      }
      /**
       * @type {() => IterableIterator<[string, string]>}
       */
      *entries() {
        for (const name of this.keys()) {
          yield [name, this.get(name)];
        }
      }
      [Symbol.iterator]() {
        return this.entries();
      }
      /**
       * Node-fetch non-spec method
       * returning all headers and their values as array
       * @returns {Record<string, string[]>}
       */
      raw() {
        return [...this.keys()].reduce((result, key) => {
          result[key] = this.getAll(key);
          return result;
        }, {});
      }
      /**
       * For better console.log(headers) and also to convert Headers into Node.js Request compatible format
       */
      [Symbol.for("nodejs.util.inspect.custom")]() {
        return [...this.keys()].reduce((result, key) => {
          const values = this.getAll(key);
          if (key === "host") {
            result[key] = values[0];
          } else {
            result[key] = values.length > 1 ? values : values[0];
          }
          return result;
        }, {});
      }
    };
    Object.defineProperties(
      Headers2.prototype,
      ["get", "entries", "forEach", "values"].reduce((result, property) => {
        result[property] = { enumerable: true };
        return result;
      }, {})
    );
  }
});

// node_modules/node-fetch/src/utils/is-redirect.js
var redirectStatus, isRedirect;
var init_is_redirect = __esm({
  "node_modules/node-fetch/src/utils/is-redirect.js"() {
    redirectStatus = /* @__PURE__ */ new Set([301, 302, 303, 307, 308]);
    isRedirect = (code) => {
      return redirectStatus.has(code);
    };
  }
});

// node_modules/node-fetch/src/response.js
var INTERNALS2, Response;
var init_response = __esm({
  "node_modules/node-fetch/src/response.js"() {
    init_headers();
    init_body();
    init_is_redirect();
    INTERNALS2 = Symbol("Response internals");
    Response = class _Response extends Body {
      constructor(body = null, options = {}) {
        super(body, options);
        const status = options.status != null ? options.status : 200;
        const headers = new Headers2(options.headers);
        if (body !== null && !headers.has("Content-Type")) {
          const contentType = extractContentType(body, this);
          if (contentType) {
            headers.append("Content-Type", contentType);
          }
        }
        this[INTERNALS2] = {
          type: "default",
          url: options.url,
          status,
          statusText: options.statusText || "",
          headers,
          counter: options.counter,
          highWaterMark: options.highWaterMark
        };
      }
      get type() {
        return this[INTERNALS2].type;
      }
      get url() {
        return this[INTERNALS2].url || "";
      }
      get status() {
        return this[INTERNALS2].status;
      }
      /**
       * Convenience property representing if the request ended normally
       */
      get ok() {
        return this[INTERNALS2].status >= 200 && this[INTERNALS2].status < 300;
      }
      get redirected() {
        return this[INTERNALS2].counter > 0;
      }
      get statusText() {
        return this[INTERNALS2].statusText;
      }
      get headers() {
        return this[INTERNALS2].headers;
      }
      get highWaterMark() {
        return this[INTERNALS2].highWaterMark;
      }
      /**
       * Clone this response
       *
       * @return  Response
       */
      clone() {
        return new _Response(clone(this, this.highWaterMark), {
          type: this.type,
          url: this.url,
          status: this.status,
          statusText: this.statusText,
          headers: this.headers,
          ok: this.ok,
          redirected: this.redirected,
          size: this.size,
          highWaterMark: this.highWaterMark
        });
      }
      /**
       * @param {string} url    The URL that the new response is to originate from.
       * @param {number} status An optional status code for the response (e.g., 302.)
       * @returns {Response}    A Response object.
       */
      static redirect(url, status = 302) {
        if (!isRedirect(status)) {
          throw new RangeError('Failed to execute "redirect" on "response": Invalid status code');
        }
        return new _Response(null, {
          headers: {
            location: new URL(url).toString()
          },
          status
        });
      }
      static error() {
        const response = new _Response(null, { status: 0, statusText: "" });
        response[INTERNALS2].type = "error";
        return response;
      }
      static json(data = void 0, init = {}) {
        const body = JSON.stringify(data);
        if (body === void 0) {
          throw new TypeError("data is not JSON serializable");
        }
        const headers = new Headers2(init && init.headers);
        if (!headers.has("content-type")) {
          headers.set("content-type", "application/json");
        }
        return new _Response(body, {
          ...init,
          headers
        });
      }
      get [Symbol.toStringTag]() {
        return "Response";
      }
    };
    Object.defineProperties(Response.prototype, {
      type: { enumerable: true },
      url: { enumerable: true },
      status: { enumerable: true },
      ok: { enumerable: true },
      redirected: { enumerable: true },
      statusText: { enumerable: true },
      headers: { enumerable: true },
      clone: { enumerable: true }
    });
  }
});

// node_modules/node-fetch/src/utils/get-search.js
var getSearch;
var init_get_search = __esm({
  "node_modules/node-fetch/src/utils/get-search.js"() {
    getSearch = (parsedURL) => {
      if (parsedURL.search) {
        return parsedURL.search;
      }
      const lastOffset = parsedURL.href.length - 1;
      const hash = parsedURL.hash || (parsedURL.href[lastOffset] === "#" ? "#" : "");
      return parsedURL.href[lastOffset - hash.length] === "?" ? "?" : "";
    };
  }
});
function stripURLForUseAsAReferrer(url, originOnly = false) {
  if (url == null) {
    return "no-referrer";
  }
  url = new URL(url);
  if (/^(about|blob|data):$/.test(url.protocol)) {
    return "no-referrer";
  }
  url.username = "";
  url.password = "";
  url.hash = "";
  if (originOnly) {
    url.pathname = "";
    url.search = "";
  }
  return url;
}
function validateReferrerPolicy(referrerPolicy) {
  if (!ReferrerPolicy.has(referrerPolicy)) {
    throw new TypeError(`Invalid referrerPolicy: ${referrerPolicy}`);
  }
  return referrerPolicy;
}
function isOriginPotentiallyTrustworthy(url) {
  if (/^(http|ws)s:$/.test(url.protocol)) {
    return true;
  }
  const hostIp = url.host.replace(/(^\[)|(]$)/g, "");
  const hostIPVersion = isIP(hostIp);
  if (hostIPVersion === 4 && /^127\./.test(hostIp)) {
    return true;
  }
  if (hostIPVersion === 6 && /^(((0+:){7})|(::(0+:){0,6}))0*1$/.test(hostIp)) {
    return true;
  }
  if (url.host === "localhost" || url.host.endsWith(".localhost")) {
    return false;
  }
  if (url.protocol === "file:") {
    return true;
  }
  return false;
}
function isUrlPotentiallyTrustworthy(url) {
  if (/^about:(blank|srcdoc)$/.test(url)) {
    return true;
  }
  if (url.protocol === "data:") {
    return true;
  }
  if (/^(blob|filesystem):$/.test(url.protocol)) {
    return true;
  }
  return isOriginPotentiallyTrustworthy(url);
}
function determineRequestsReferrer(request, { referrerURLCallback, referrerOriginCallback } = {}) {
  if (request.referrer === "no-referrer" || request.referrerPolicy === "") {
    return null;
  }
  const policy = request.referrerPolicy;
  if (request.referrer === "about:client") {
    return "no-referrer";
  }
  const referrerSource = request.referrer;
  let referrerURL = stripURLForUseAsAReferrer(referrerSource);
  let referrerOrigin = stripURLForUseAsAReferrer(referrerSource, true);
  if (referrerURL.toString().length > 4096) {
    referrerURL = referrerOrigin;
  }
  if (referrerURLCallback) {
    referrerURL = referrerURLCallback(referrerURL);
  }
  if (referrerOriginCallback) {
    referrerOrigin = referrerOriginCallback(referrerOrigin);
  }
  const currentURL = new URL(request.url);
  switch (policy) {
    case "no-referrer":
      return "no-referrer";
    case "origin":
      return referrerOrigin;
    case "unsafe-url":
      return referrerURL;
    case "strict-origin":
      if (isUrlPotentiallyTrustworthy(referrerURL) && !isUrlPotentiallyTrustworthy(currentURL)) {
        return "no-referrer";
      }
      return referrerOrigin.toString();
    case "strict-origin-when-cross-origin":
      if (referrerURL.origin === currentURL.origin) {
        return referrerURL;
      }
      if (isUrlPotentiallyTrustworthy(referrerURL) && !isUrlPotentiallyTrustworthy(currentURL)) {
        return "no-referrer";
      }
      return referrerOrigin;
    case "same-origin":
      if (referrerURL.origin === currentURL.origin) {
        return referrerURL;
      }
      return "no-referrer";
    case "origin-when-cross-origin":
      if (referrerURL.origin === currentURL.origin) {
        return referrerURL;
      }
      return referrerOrigin;
    case "no-referrer-when-downgrade":
      if (isUrlPotentiallyTrustworthy(referrerURL) && !isUrlPotentiallyTrustworthy(currentURL)) {
        return "no-referrer";
      }
      return referrerURL;
    default:
      throw new TypeError(`Invalid referrerPolicy: ${policy}`);
  }
}
function parseReferrerPolicyFromHeader(headers) {
  const policyTokens = (headers.get("referrer-policy") || "").split(/[,\s]+/);
  let policy = "";
  for (const token of policyTokens) {
    if (token && ReferrerPolicy.has(token)) {
      policy = token;
    }
  }
  return policy;
}
var ReferrerPolicy, DEFAULT_REFERRER_POLICY;
var init_referrer = __esm({
  "node_modules/node-fetch/src/utils/referrer.js"() {
    ReferrerPolicy = /* @__PURE__ */ new Set([
      "",
      "no-referrer",
      "no-referrer-when-downgrade",
      "same-origin",
      "origin",
      "strict-origin",
      "origin-when-cross-origin",
      "strict-origin-when-cross-origin",
      "unsafe-url"
    ]);
    DEFAULT_REFERRER_POLICY = "strict-origin-when-cross-origin";
  }
});
var INTERNALS3, isRequest, doBadDataWarn, Request, getNodeRequestOptions;
var init_request = __esm({
  "node_modules/node-fetch/src/request.js"() {
    init_headers();
    init_body();
    init_is();
    init_get_search();
    init_referrer();
    INTERNALS3 = Symbol("Request internals");
    isRequest = (object) => {
      return typeof object === "object" && typeof object[INTERNALS3] === "object";
    };
    doBadDataWarn = deprecate(
      () => {
      },
      ".data is not a valid RequestInit property, use .body instead",
      "https://github.com/node-fetch/node-fetch/issues/1000 (request)"
    );
    Request = class _Request extends Body {
      constructor(input, init = {}) {
        let parsedURL;
        if (isRequest(input)) {
          parsedURL = new URL(input.url);
        } else {
          parsedURL = new URL(input);
          input = {};
        }
        if (parsedURL.username !== "" || parsedURL.password !== "") {
          throw new TypeError(`${parsedURL} is an url with embedded credentials.`);
        }
        let method = init.method || input.method || "GET";
        if (/^(delete|get|head|options|post|put)$/i.test(method)) {
          method = method.toUpperCase();
        }
        if (!isRequest(init) && "data" in init) {
          doBadDataWarn();
        }
        if ((init.body != null || isRequest(input) && input.body !== null) && (method === "GET" || method === "HEAD")) {
          throw new TypeError("Request with GET/HEAD method cannot have body");
        }
        const inputBody = init.body ? init.body : isRequest(input) && input.body !== null ? clone(input) : null;
        super(inputBody, {
          size: init.size || input.size || 0
        });
        const headers = new Headers2(init.headers || input.headers || {});
        if (inputBody !== null && !headers.has("Content-Type")) {
          const contentType = extractContentType(inputBody, this);
          if (contentType) {
            headers.set("Content-Type", contentType);
          }
        }
        let signal = isRequest(input) ? input.signal : null;
        if ("signal" in init) {
          signal = init.signal;
        }
        if (signal != null && !isAbortSignal(signal)) {
          throw new TypeError("Expected signal to be an instanceof AbortSignal or EventTarget");
        }
        let referrer = init.referrer == null ? input.referrer : init.referrer;
        if (referrer === "") {
          referrer = "no-referrer";
        } else if (referrer) {
          const parsedReferrer = new URL(referrer);
          referrer = /^about:(\/\/)?client$/.test(parsedReferrer) ? "client" : parsedReferrer;
        } else {
          referrer = void 0;
        }
        this[INTERNALS3] = {
          method,
          redirect: init.redirect || input.redirect || "follow",
          headers,
          parsedURL,
          signal,
          referrer
        };
        this.follow = init.follow === void 0 ? input.follow === void 0 ? 20 : input.follow : init.follow;
        this.compress = init.compress === void 0 ? input.compress === void 0 ? true : input.compress : init.compress;
        this.counter = init.counter || input.counter || 0;
        this.agent = init.agent || input.agent;
        this.highWaterMark = init.highWaterMark || input.highWaterMark || 16384;
        this.insecureHTTPParser = init.insecureHTTPParser || input.insecureHTTPParser || false;
        this.referrerPolicy = init.referrerPolicy || input.referrerPolicy || "";
      }
      /** @returns {string} */
      get method() {
        return this[INTERNALS3].method;
      }
      /** @returns {string} */
      get url() {
        return format(this[INTERNALS3].parsedURL);
      }
      /** @returns {Headers} */
      get headers() {
        return this[INTERNALS3].headers;
      }
      get redirect() {
        return this[INTERNALS3].redirect;
      }
      /** @returns {AbortSignal} */
      get signal() {
        return this[INTERNALS3].signal;
      }
      // https://fetch.spec.whatwg.org/#dom-request-referrer
      get referrer() {
        if (this[INTERNALS3].referrer === "no-referrer") {
          return "";
        }
        if (this[INTERNALS3].referrer === "client") {
          return "about:client";
        }
        if (this[INTERNALS3].referrer) {
          return this[INTERNALS3].referrer.toString();
        }
        return void 0;
      }
      get referrerPolicy() {
        return this[INTERNALS3].referrerPolicy;
      }
      set referrerPolicy(referrerPolicy) {
        this[INTERNALS3].referrerPolicy = validateReferrerPolicy(referrerPolicy);
      }
      /**
       * Clone this request
       *
       * @return  Request
       */
      clone() {
        return new _Request(this);
      }
      get [Symbol.toStringTag]() {
        return "Request";
      }
    };
    Object.defineProperties(Request.prototype, {
      method: { enumerable: true },
      url: { enumerable: true },
      headers: { enumerable: true },
      redirect: { enumerable: true },
      clone: { enumerable: true },
      signal: { enumerable: true },
      referrer: { enumerable: true },
      referrerPolicy: { enumerable: true }
    });
    getNodeRequestOptions = (request) => {
      const { parsedURL } = request[INTERNALS3];
      const headers = new Headers2(request[INTERNALS3].headers);
      if (!headers.has("Accept")) {
        headers.set("Accept", "*/*");
      }
      let contentLengthValue = null;
      if (request.body === null && /^(post|put)$/i.test(request.method)) {
        contentLengthValue = "0";
      }
      if (request.body !== null) {
        const totalBytes = getTotalBytes(request);
        if (typeof totalBytes === "number" && !Number.isNaN(totalBytes)) {
          contentLengthValue = String(totalBytes);
        }
      }
      if (contentLengthValue) {
        headers.set("Content-Length", contentLengthValue);
      }
      if (request.referrerPolicy === "") {
        request.referrerPolicy = DEFAULT_REFERRER_POLICY;
      }
      if (request.referrer && request.referrer !== "no-referrer") {
        request[INTERNALS3].referrer = determineRequestsReferrer(request);
      } else {
        request[INTERNALS3].referrer = "no-referrer";
      }
      if (request[INTERNALS3].referrer instanceof URL) {
        headers.set("Referer", request.referrer);
      }
      if (!headers.has("User-Agent")) {
        headers.set("User-Agent", "node-fetch");
      }
      if (request.compress && !headers.has("Accept-Encoding")) {
        headers.set("Accept-Encoding", "gzip, deflate, br");
      }
      let { agent } = request;
      if (typeof agent === "function") {
        agent = agent(parsedURL);
      }
      const search = getSearch(parsedURL);
      const options = {
        // Overwrite search to retain trailing ? (issue #776)
        path: parsedURL.pathname + search,
        // The following options are not expressed in the URL
        method: request.method,
        headers: headers[Symbol.for("nodejs.util.inspect.custom")](),
        insecureHTTPParser: request.insecureHTTPParser,
        agent
      };
      return {
        /** @type {URL} */
        parsedURL,
        options
      };
    };
  }
});

// node_modules/node-fetch/src/errors/abort-error.js
var AbortError;
var init_abort_error = __esm({
  "node_modules/node-fetch/src/errors/abort-error.js"() {
    init_base();
    AbortError = class extends FetchBaseError {
      constructor(message, type = "aborted") {
        super(message, type);
      }
    };
  }
});

// node_modules/node-fetch/src/index.js
var src_exports = {};
__export(src_exports, {
  AbortError: () => AbortError,
  Blob: () => fetch_blob_default,
  FetchError: () => FetchError,
  File: () => file_default,
  FormData: () => FormData,
  Headers: () => Headers2,
  Request: () => Request,
  Response: () => Response,
  blobFrom: () => blobFrom,
  blobFromSync: () => blobFromSync,
  default: () => fetch2,
  fileFrom: () => fileFrom,
  fileFromSync: () => fileFromSync,
  isRedirect: () => isRedirect
});
async function fetch2(url, options_) {
  return new Promise((resolve, reject) => {
    const request = new Request(url, options_);
    const { parsedURL, options } = getNodeRequestOptions(request);
    if (!supportedSchemas.has(parsedURL.protocol)) {
      throw new TypeError(`node-fetch cannot load ${url}. URL scheme "${parsedURL.protocol.replace(/:$/, "")}" is not supported.`);
    }
    if (parsedURL.protocol === "data:") {
      const data = dist_default(request.url);
      const response2 = new Response(data, { headers: { "Content-Type": data.typeFull } });
      resolve(response2);
      return;
    }
    const send = (parsedURL.protocol === "https:" ? https : http).request;
    const { signal } = request;
    let response = null;
    const abort = () => {
      const error = new AbortError("The operation was aborted.");
      reject(error);
      if (request.body && request.body instanceof Stream.Readable) {
        request.body.destroy(error);
      }
      if (!response || !response.body) {
        return;
      }
      response.body.emit("error", error);
    };
    if (signal && signal.aborted) {
      abort();
      return;
    }
    const abortAndFinalize = () => {
      abort();
      finalize();
    };
    const request_ = send(parsedURL.toString(), options);
    if (signal) {
      signal.addEventListener("abort", abortAndFinalize);
    }
    const finalize = () => {
      request_.abort();
      if (signal) {
        signal.removeEventListener("abort", abortAndFinalize);
      }
    };
    request_.on("error", (error) => {
      reject(new FetchError(`request to ${request.url} failed, reason: ${error.message}`, "system", error));
      finalize();
    });
    fixResponseChunkedTransferBadEnding(request_, (error) => {
      if (response && response.body) {
        response.body.destroy(error);
      }
    });
    if (process.version < "v14") {
      request_.on("socket", (s2) => {
        let endedWithEventsCount;
        s2.prependListener("end", () => {
          endedWithEventsCount = s2._eventsCount;
        });
        s2.prependListener("close", (hadError) => {
          if (response && endedWithEventsCount < s2._eventsCount && !hadError) {
            const error = new Error("Premature close");
            error.code = "ERR_STREAM_PREMATURE_CLOSE";
            response.body.emit("error", error);
          }
        });
      });
    }
    request_.on("response", (response_) => {
      request_.setTimeout(0);
      const headers = fromRawHeaders(response_.rawHeaders);
      if (isRedirect(response_.statusCode)) {
        const location = headers.get("Location");
        let locationURL = null;
        try {
          locationURL = location === null ? null : new URL(location, request.url);
        } catch {
          if (request.redirect !== "manual") {
            reject(new FetchError(`uri requested responds with an invalid redirect URL: ${location}`, "invalid-redirect"));
            finalize();
            return;
          }
        }
        switch (request.redirect) {
          case "error":
            reject(new FetchError(`uri requested responds with a redirect, redirect mode is set to error: ${request.url}`, "no-redirect"));
            finalize();
            return;
          case "manual":
            break;
          case "follow": {
            if (locationURL === null) {
              break;
            }
            if (request.counter >= request.follow) {
              reject(new FetchError(`maximum redirect reached at: ${request.url}`, "max-redirect"));
              finalize();
              return;
            }
            const requestOptions = {
              headers: new Headers2(request.headers),
              follow: request.follow,
              counter: request.counter + 1,
              agent: request.agent,
              compress: request.compress,
              method: request.method,
              body: clone(request),
              signal: request.signal,
              size: request.size,
              referrer: request.referrer,
              referrerPolicy: request.referrerPolicy
            };
            if (!isDomainOrSubdomain(request.url, locationURL) || !isSameProtocol(request.url, locationURL)) {
              for (const name of ["authorization", "www-authenticate", "cookie", "cookie2"]) {
                requestOptions.headers.delete(name);
              }
            }
            if (response_.statusCode !== 303 && request.body && options_.body instanceof Stream.Readable) {
              reject(new FetchError("Cannot follow redirect with body being a readable stream", "unsupported-redirect"));
              finalize();
              return;
            }
            if (response_.statusCode === 303 || (response_.statusCode === 301 || response_.statusCode === 302) && request.method === "POST") {
              requestOptions.method = "GET";
              requestOptions.body = void 0;
              requestOptions.headers.delete("content-length");
            }
            const responseReferrerPolicy = parseReferrerPolicyFromHeader(headers);
            if (responseReferrerPolicy) {
              requestOptions.referrerPolicy = responseReferrerPolicy;
            }
            resolve(fetch2(new Request(locationURL, requestOptions)));
            finalize();
            return;
          }
          default:
            return reject(new TypeError(`Redirect option '${request.redirect}' is not a valid value of RequestRedirect`));
        }
      }
      if (signal) {
        response_.once("end", () => {
          signal.removeEventListener("abort", abortAndFinalize);
        });
      }
      let body = pipeline$1(response_, new PassThrough(), (error) => {
        if (error) {
          reject(error);
        }
      });
      if (process.version < "v12.10") {
        response_.on("aborted", abortAndFinalize);
      }
      const responseOptions = {
        url: request.url,
        status: response_.statusCode,
        statusText: response_.statusMessage,
        headers,
        size: request.size,
        counter: request.counter,
        highWaterMark: request.highWaterMark
      };
      const codings = headers.get("Content-Encoding");
      if (!request.compress || request.method === "HEAD" || codings === null || response_.statusCode === 204 || response_.statusCode === 304) {
        response = new Response(body, responseOptions);
        resolve(response);
        return;
      }
      const zlibOptions = {
        flush: zlib.Z_SYNC_FLUSH,
        finishFlush: zlib.Z_SYNC_FLUSH
      };
      if (codings === "gzip" || codings === "x-gzip") {
        body = pipeline$1(body, zlib.createGunzip(zlibOptions), (error) => {
          if (error) {
            reject(error);
          }
        });
        response = new Response(body, responseOptions);
        resolve(response);
        return;
      }
      if (codings === "deflate" || codings === "x-deflate") {
        const raw = pipeline$1(response_, new PassThrough(), (error) => {
          if (error) {
            reject(error);
          }
        });
        raw.once("data", (chunk) => {
          if ((chunk[0] & 15) === 8) {
            body = pipeline$1(body, zlib.createInflate(), (error) => {
              if (error) {
                reject(error);
              }
            });
          } else {
            body = pipeline$1(body, zlib.createInflateRaw(), (error) => {
              if (error) {
                reject(error);
              }
            });
          }
          response = new Response(body, responseOptions);
          resolve(response);
        });
        raw.once("end", () => {
          if (!response) {
            response = new Response(body, responseOptions);
            resolve(response);
          }
        });
        return;
      }
      if (codings === "br") {
        body = pipeline$1(body, zlib.createBrotliDecompress(), (error) => {
          if (error) {
            reject(error);
          }
        });
        response = new Response(body, responseOptions);
        resolve(response);
        return;
      }
      response = new Response(body, responseOptions);
      resolve(response);
    });
    writeToStream(request_, request).catch(reject);
  });
}
function fixResponseChunkedTransferBadEnding(request, errorCallback) {
  const LAST_CHUNK = Buffer$1.from("0\r\n\r\n");
  let isChunkedTransfer = false;
  let properLastChunkReceived = false;
  let previousChunk;
  request.on("response", (response) => {
    const { headers } = response;
    isChunkedTransfer = headers["transfer-encoding"] === "chunked" && !headers["content-length"];
  });
  request.on("socket", (socket) => {
    const onSocketClose = () => {
      if (isChunkedTransfer && !properLastChunkReceived) {
        const error = new Error("Premature close");
        error.code = "ERR_STREAM_PREMATURE_CLOSE";
        errorCallback(error);
      }
    };
    const onData = (buf) => {
      properLastChunkReceived = Buffer$1.compare(buf.slice(-5), LAST_CHUNK) === 0;
      if (!properLastChunkReceived && previousChunk) {
        properLastChunkReceived = Buffer$1.compare(previousChunk.slice(-3), LAST_CHUNK.slice(0, 3)) === 0 && Buffer$1.compare(buf.slice(-2), LAST_CHUNK.slice(3)) === 0;
      }
      previousChunk = buf;
    };
    socket.prependListener("close", onSocketClose);
    socket.on("data", onData);
    request.on("close", () => {
      socket.removeListener("close", onSocketClose);
      socket.removeListener("data", onData);
    });
  });
}
var supportedSchemas;
var init_src = __esm({
  "node_modules/node-fetch/src/index.js"() {
    init_dist();
    init_body();
    init_response();
    init_headers();
    init_request();
    init_fetch_error();
    init_abort_error();
    init_is_redirect();
    init_esm_min();
    init_is();
    init_referrer();
    init_from();
    supportedSchemas = /* @__PURE__ */ new Set(["data:", "http:", "https:"]);
  }
});

// src/http-client.ts
var isNode = typeof process !== "undefined" && process.versions && process.versions.node;
var isBrowser = typeof window !== "undefined" && typeof window.fetch === "function";
var HttpClient = class {
  fetch;
  HeadersClass;
  constructor() {
    this.initializeEnvironment();
  }
  initializeEnvironment() {
    if (isNode) {
      this.initializeNodeEnvironment();
    } else if (isBrowser) {
      this.fetch = globalThis.fetch;
      this.HeadersClass = globalThis.Headers;
    } else {
      this.fetch = globalThis.fetch;
      this.HeadersClass = globalThis.Headers;
    }
  }
  initializeNodeEnvironment() {
    if (typeof globalThis.fetch === "function" && typeof globalThis.Headers === "function") {
      this.fetch = globalThis.fetch;
      this.HeadersClass = globalThis.Headers;
      return;
    }
    try {
      const nodeFetch = (init_src(), __toCommonJS(src_exports));
      const { Headers: NodeHeaders } = nodeFetch;
      this.fetch = nodeFetch.default || nodeFetch;
      this.HeadersClass = NodeHeaders;
    } catch (error) {
      throw new Error(
        "X API SDK: node-fetch not found. For Node.js environments, please install node-fetch:\nnpm install node-fetch\nOr upgrade to Node.js 18+ for native fetch support."
      );
    }
  }
  /**
   * Create a new Headers instance
   */
  createHeaders(init) {
    return new this.HeadersClass(init);
  }
  /**
   * Make an HTTP request
   */
  async request(url, options = {}) {
    let body = options.body;
    if (body && typeof body !== "string") {
      if (Buffer.isBuffer(body)) {
        body = body.toString();
      } else if (body instanceof ArrayBuffer) {
        body = new TextDecoder().decode(body);
      } else if (ArrayBuffer.isView(body)) {
        body = new TextDecoder().decode(body);
      }
    }
    let signal = options.signal;
    if (options.timeout && options.timeout > 0 && !signal) {
      const controller = new AbortController();
      setTimeout(() => controller.abort(), options.timeout);
      signal = controller.signal;
    }
    const response = await this.fetch(url, {
      method: options.method || "GET",
      headers: options.headers,
      body,
      signal
    });
    return response;
  }
  /**
   * Make a GET request
   */
  async get(url, headers) {
    return this.request(url, {
      method: "GET",
      headers
    });
  }
  /**
   * Make a POST request
   */
  async post(url, body, headers) {
    return this.request(url, {
      method: "POST",
      headers,
      body
    });
  }
  /**
   * Make a PUT request
   */
  async put(url, body, headers) {
    return this.request(url, {
      method: "PUT",
      headers,
      body
    });
  }
  /**
   * Make a DELETE request
   */
  async delete(url, headers) {
    return this.request(url, {
      method: "DELETE",
      headers
    });
  }
  /**
   * Make a PATCH request
   */
  async patch(url, body, headers) {
    return this.request(url, {
      method: "PATCH",
      headers,
      body
    });
  }
};
var httpClient = new HttpClient();

// src/activity/client.ts
var ActivityClient = class {
  client;
  /**
     * Creates a new activity client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get X activity subscriptions
     * Get a list of active subscriptions for XAA
  
  
  
     * @returns {Promise<GetSubscriptionsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getSubscriptions() {
    let path = "/2/activity/subscriptions";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create X activity subscription
     * Creates a subscription for an X activity event
  
  
  
     * @returns {Promise<CreateSubscriptionResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createSubscription(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/activity/subscriptions";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Activity Stream
     * Stream of X Activities
  
  
  
     * @returns {Promise<StreamResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async stream(options = {}) {
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/activity/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Update X activity subscription
     * Updates a subscription for an X activity event
  
  
     * @param subscriptionId The ID of the subscription to update.
  
  
  
  
     * @returns {Promise<UpdateSubscriptionResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async updateSubscription(subscriptionId, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/activity/subscriptions/{subscription_id}";
    path = path.replace(
      "{subscription_id}",
      encodeURIComponent(String(subscriptionId))
    );
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "PUT",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Deletes X activity subscription
     * Deletes a subscription for an X activity event
  
  
     * @param subscriptionId The ID of the subscription to delete.
  
  
  
  
     * @returns {Promise<DeleteSubscriptionResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async deleteSubscription(subscriptionId) {
    let path = "/2/activity/subscriptions/{subscription_id}";
    path = path.replace(
      "{subscription_id}",
      encodeURIComponent(String(subscriptionId))
    );
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/activity/models.ts
var models_exports = {};

// src/news/client.ts
var NewsClient = class {
  client;
  /**
     * Creates a new news client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get news stories by ID
     * Retrieves news story by its ID.
  
  
     * @param id The ID of the news story.
  
  
  
  
     * @returns {Promise<GetResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async get(id, options = {}) {
    const paramMappings = {
      "news.fields": "newsFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      newsFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/news/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (newsFields !== void 0 && newsFields.length > 0) {
      params.append("news.fields", newsFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Search News
     * Retrieves a list of News stories matching the specified search query.
  
  
  
     * @param query The search query.
  
  
  
     * @returns {Promise<SearchResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async search(query, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      max_age_hours: "maxAgeHours",
      "news.fields": "newsFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      maxAgeHours = void 0,
      newsFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/news/search";
    const params = new URLSearchParams();
    if (query !== void 0) {
      params.append("query", String(query));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (maxAgeHours !== void 0) {
      params.append("max_age_hours", String(maxAgeHours));
    }
    if (newsFields !== void 0 && newsFields.length > 0) {
      params.append("news.fields", newsFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/news/models.ts
var models_exports2 = {};

// src/connections/client.ts
var ConnectionsClient = class {
  client;
  /**
     * Creates a new connections client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Terminate all connections
     * Terminates all active streaming connections for the authenticated application.
  
  
  
     * @returns {Promise<DeleteAllResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async deleteAll() {
    let path = "/2/connections/all";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/connections/models.ts
var models_exports3 = {};

// src/account_activity/client.ts
var AccountActivityClient = class {
  client;
  /**
     * Creates a new account activity client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get subscriptions
     * Retrieves a list of all active subscriptions for a given webhook.
  
  
     * @param webhookId The webhook ID to pull subscriptions for.
  
  
  
  
     * @returns {Promise<GetSubscriptionsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getSubscriptions(webhookId) {
    let path = "/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list";
    path = path.replace("{webhook_id}", encodeURIComponent(String(webhookId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Validate subscription
     * Checks a user’s Account Activity subscription for a given webhook.
  
  
     * @param webhookId The webhook ID to check subscription against.
  
  
  
  
     * @returns {Promise<ValidateSubscriptionResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async validateSubscription(webhookId) {
    let path = "/2/account_activity/webhooks/{webhook_id}/subscriptions/all";
    path = path.replace("{webhook_id}", encodeURIComponent(String(webhookId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.read", "dm.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create subscription
     * Creates an Account Activity subscription for the user and the given webhook.
  
  
     * @param webhookId The webhook ID to check subscription against.
  
  
  
  
     * @returns {Promise<CreateSubscriptionResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createSubscription(webhookId, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/account_activity/webhooks/{webhook_id}/subscriptions/all";
    path = path.replace("{webhook_id}", encodeURIComponent(String(webhookId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.read", "dm.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get subscription count
     * Retrieves a count of currently active Account Activity subscriptions.
  
  
  
     * @returns {Promise<GetSubscriptionCountResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getSubscriptionCount() {
    let path = "/2/account_activity/subscriptions/count";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Delete subscription
     * Deletes an Account Activity subscription for the given webhook and user ID.
  
  
     * @param webhookId The webhook ID to check subscription against.
  
  
  
     * @param userId User ID to unsubscribe from.
  
  
  
  
     * @returns {Promise<DeleteSubscriptionResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async deleteSubscription(webhookId, userId) {
    let path = "/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all";
    path = path.replace("{webhook_id}", encodeURIComponent(String(webhookId)));
    path = path.replace("{user_id}", encodeURIComponent(String(userId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create replay job
     * Creates a replay job to retrieve activities from up to the past 5 days for all subscriptions associated with a given webhook.
  
  
     * @param webhookId The unique identifier for the webhook configuration.
  
  
  
  
     * @param fromDate The oldest (starting) UTC timestamp (inclusive) from which events will be provided, in `yyyymmddhhmm` format.
  
  
  
     * @param toDate The latest (ending) UTC timestamp (exclusive) up to which events will be provided, in `yyyymmddhhmm` format.
  
  
  
     * @returns {Promise<CreateReplayJobResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createReplayJob(webhookId, fromDate, toDate) {
    let path = "/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all";
    path = path.replace("{webhook_id}", encodeURIComponent(String(webhookId)));
    const params = new URLSearchParams();
    if (fromDate !== void 0) {
      params.append("from_date", String(fromDate));
    }
    if (toDate !== void 0) {
      params.append("to_date", String(toDate));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/account_activity/models.ts
var models_exports4 = {};

// src/spaces/client.ts
var SpacesClient = class {
  client;
  /**
     * Creates a new spaces client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get space by ID
     * Retrieves details of a specific space by its ID.
  
  
     * @param id The ID of the Space to be retrieved.
  
  
  
  
     * @returns {Promise<GetByIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getById(id, options = {}) {
    const paramMappings = {
      "space.fields": "spaceFields",
      "user.fields": "userFields",
      "topic.fields": "topicFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      spaceFields = [],
      expansions = [],
      userFields = [],
      topicFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/spaces/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (spaceFields !== void 0 && spaceFields.length > 0) {
      params.append("space.fields", spaceFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (topicFields !== void 0 && topicFields.length > 0) {
      params.append("topic.fields", topicFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["space.read", "tweet.read", "users.read"]
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Space ticket buyers
     * Retrieves a list of Users who purchased tickets to a specific Space by its ID.
  
  
     * @param id The ID of the Space to be retrieved.
  
  
  
  
     * @returns {Promise<GetBuyersResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getBuyers(id, options = {}) {
    const paramMappings = {
      pagination_token: "paginationToken",
      max_results: "maxResults",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      paginationToken = void 0,
      maxResults = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/spaces/{id}/buyers";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["space.read", "tweet.read", "users.read"]
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Space Posts
     * Retrieves a list of Posts shared in a specific Space by its ID.
  
  
     * @param id The ID of the Space to be retrieved.
  
  
  
  
     * @returns {Promise<GetPostsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getPosts(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/spaces/{id}/tweets";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["space.read", "tweet.read", "users.read"]
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Spaces by creator IDs
     * Retrieves details of Spaces created by specified User IDs.
  
  
  
     * @param userIds The IDs of Users to search through.
  
  
  
     * @returns {Promise<GetByCreatorIdsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getByCreatorIds(userIds, options = {}) {
    const paramMappings = {
      "space.fields": "spaceFields",
      "user.fields": "userFields",
      "topic.fields": "topicFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      spaceFields = [],
      expansions = [],
      userFields = [],
      topicFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/spaces/by/creator_ids";
    const params = new URLSearchParams();
    if (userIds !== void 0 && userIds.length > 0) {
      params.append("user_ids", userIds.join(","));
    }
    if (spaceFields !== void 0 && spaceFields.length > 0) {
      params.append("space.fields", spaceFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (topicFields !== void 0 && topicFields.length > 0) {
      params.append("topic.fields", topicFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["space.read", "tweet.read", "users.read"]
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Spaces by IDs
     * Retrieves details of multiple Spaces by their IDs.
  
  
  
     * @param ids The list of Space IDs to return.
  
  
  
     * @returns {Promise<GetByIdsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getByIds(ids, options = {}) {
    const paramMappings = {
      "space.fields": "spaceFields",
      "user.fields": "userFields",
      "topic.fields": "topicFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      spaceFields = [],
      expansions = [],
      userFields = [],
      topicFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/spaces";
    const params = new URLSearchParams();
    if (ids !== void 0 && ids.length > 0) {
      params.append("ids", ids.join(","));
    }
    if (spaceFields !== void 0 && spaceFields.length > 0) {
      params.append("space.fields", spaceFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (topicFields !== void 0 && topicFields.length > 0) {
      params.append("topic.fields", topicFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["space.read", "tweet.read", "users.read"]
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Search Spaces
     * Retrieves a list of Spaces matching the specified search query.
  
  
  
     * @param query The search query.
  
  
  
     * @returns {Promise<SearchResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async search(query, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      "space.fields": "spaceFields",
      "user.fields": "userFields",
      "topic.fields": "topicFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      state = void 0,
      maxResults = void 0,
      spaceFields = [],
      expansions = [],
      userFields = [],
      topicFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/spaces/search";
    const params = new URLSearchParams();
    if (query !== void 0) {
      params.append("query", String(query));
    }
    if (state !== void 0) {
      params.append("state", String(state));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (spaceFields !== void 0 && spaceFields.length > 0) {
      params.append("space.fields", spaceFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (topicFields !== void 0 && topicFields.length > 0) {
      params.append("topic.fields", topicFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["space.read", "tweet.read", "users.read"]
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/spaces/models.ts
var models_exports5 = {};

// src/trends/client.ts
var TrendsClient = class {
  client;
  /**
     * Creates a new trends client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get personalized Trends
     * Retrieves personalized trending topics for the authenticated user.
  
  
  
     * @returns {Promise<GetPersonalizedResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getPersonalized(options = {}) {
    const paramMappings = {
      "personalized_trend.fields": "personalizedTrendFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      personalizedTrendFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/personalized_trends";
    const params = new URLSearchParams();
    if (personalizedTrendFields !== void 0 && personalizedTrendFields.length > 0) {
      params.append(
        "personalized_trend.fields",
        personalizedTrendFields.join(",")
      );
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Trends by WOEID
     * Retrieves trending topics for a specific location identified by its WOEID.
  
  
     * @param woeid The WOEID of the place to lookup a trend for.
  
  
  
  
     * @returns {Promise<GetByWoeidResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getByWoeid(woeid, options = {}) {
    const paramMappings = {
      max_trends: "maxTrends",
      "trend.fields": "trendFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxTrends = void 0,
      trendFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/trends/by/woeid/{woeid}";
    path = path.replace("{woeid}", encodeURIComponent(String(woeid)));
    const params = new URLSearchParams();
    if (maxTrends !== void 0) {
      params.append("max_trends", String(maxTrends));
    }
    if (trendFields !== void 0 && trendFields.length > 0) {
      params.append("trend.fields", trendFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get AI Trends by ID
     * Retrieves an AI trend by its ID.
  
  
     * @param id The ID of the ai trend.
  
  
  
  
     * @returns {Promise<GetAiResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getAi(id, options = {}) {
    const paramMappings = {
      "news.fields": "newsFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      newsFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/ai_trends/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (newsFields !== void 0 && newsFields.length > 0) {
      params.append("news.fields", newsFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/trends/models.ts
var models_exports6 = {};

// src/media/client.ts
var MediaClient = class {
  client;
  /**
     * Creates a new media client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get Media by media key
     * Retrieves details of a specific Media file by its media key.
  
  
     * @param mediaKey A single Media Key.
  
  
  
  
     * @returns {Promise<GetByKeyResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getByKey(mediaKey, options = {}) {
    const paramMappings = {
      "media.fields": "mediaFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      mediaFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media/{media_key}";
    path = path.replace("{media_key}", encodeURIComponent(String(mediaKey)));
    const params = new URLSearchParams();
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create Media metadata
     * Creates metadata for a Media file.
  
  
  
     * @returns {Promise<CreateMetadataResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createMetadata(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media/metadata";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["media.write"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Finalize Media upload
     * Finalizes a Media upload request.
  
  
     * @param id The media id of the targeted media to finalize.
  
  
  
  
     * @returns {Promise<FinalizeUploadResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async finalizeUpload(id) {
    let path = "/2/media/upload/{id}/finalize";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["media.write"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Append Media upload
     * Appends data to a Media upload request.
  
  
     * @param id The media identifier for the media to perform the append operation.
  
  
  
  
     * @returns {Promise<AppendUploadResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async appendUpload(id, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media/upload/{id}/append";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["media.write"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Initialize media upload
     * Initializes a media upload.
  
  
  
     * @returns {Promise<InitializeUploadResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async initializeUpload(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media/upload/initialize";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["media.write"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Media by media keys
     * Retrieves details of Media files by their media keys.
  
  
  
     * @param mediaKeys A comma separated list of Media Keys. Up to 100 are allowed in a single request.
  
  
  
     * @returns {Promise<GetByKeysResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getByKeys(mediaKeys, options = {}) {
    const paramMappings = {
      "media.fields": "mediaFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      mediaFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media";
    const params = new URLSearchParams();
    if (mediaKeys !== void 0 && mediaKeys.length > 0) {
      params.append("media_keys", mediaKeys.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Media upload status
     * Retrieves the status of a Media upload by its ID.
  
  
  
     * @param mediaId Media id for the requested media upload status.
  
  
  
     * @returns {Promise<GetUploadStatusResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getUploadStatus(mediaId, options = {}) {
    const paramMappings = {};
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      command = void 0,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media/upload";
    const params = new URLSearchParams();
    if (mediaId !== void 0) {
      params.append("media_id", String(mediaId));
    }
    if (command !== void 0) {
      params.append("command", String(command));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["media.write"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Upload media
     * Uploads a media file for use in posts or other content.
  
  
  
     * @returns {Promise<UploadResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async upload(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media/upload";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["media.write"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Media analytics
     * Retrieves analytics data for media.
  
  
  
     * @param mediaKeys A comma separated list of Media Keys. Up to 100 are allowed in a single request.
  
  
  
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
  
  
  
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
  
  
  
     * @param granularity The granularity for the search counts results.
  
  
  
     * @returns {Promise<GetAnalyticsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getAnalytics(mediaKeys, endTime, startTime, granularity, options = {}) {
    const paramMappings = {
      "media_analytics.fields": "mediaAnalyticsFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      mediaAnalyticsFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media/analytics";
    const params = new URLSearchParams();
    if (mediaKeys !== void 0 && mediaKeys.length > 0) {
      params.append("media_keys", mediaKeys.join(","));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (granularity !== void 0) {
      params.append("granularity", String(granularity));
    }
    if (mediaAnalyticsFields !== void 0 && mediaAnalyticsFields.length > 0) {
      params.append("media_analytics.fields", mediaAnalyticsFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create Media subtitles
     * Creates subtitles for a specific Media file.
  
  
  
     * @returns {Promise<CreateSubtitlesResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createSubtitles(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media/subtitles";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["media.write"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Delete Media subtitles
     * Deletes subtitles for a specific Media file.
  
  
  
     * @returns {Promise<DeleteSubtitlesResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async deleteSubtitles(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/media/subtitles";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["media.write"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/media/models.ts
var models_exports7 = {};

// src/direct_messages/client.ts
var DirectMessagesClient = class {
  client;
  /**
     * Creates a new direct messages client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Create DM message by participant ID
     * Sends a new direct message to a specific participant by their ID.
  
  
     * @param participantId The ID of the recipient user that will receive the DM.
  
  
  
  
     * @returns {Promise<CreateByParticipantIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createByParticipantId(participantId, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/dm_conversations/with/{participant_id}/messages";
    path = path.replace(
      "{participant_id}",
      encodeURIComponent(String(participantId))
    );
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get DM events
     * Retrieves a list of recent direct message events across all conversations.
  
  
  
     * @returns {Promise<GetEventsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getEvents(options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      event_types: "eventTypes",
      "dm_event.fields": "dmEventFields",
      "media.fields": "mediaFields",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      eventTypes = [],
      dmEventFields = [],
      expansions = [],
      mediaFields = [],
      userFields = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/dm_events";
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (eventTypes !== void 0 && eventTypes.length > 0) {
      params.append("event_types", eventTypes.join(","));
    }
    if (dmEventFields !== void 0 && dmEventFields.length > 0) {
      params.append("dm_event.fields", dmEventFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get DM events for a DM conversation
     * Retrieves direct message events for a specific conversation.
  
  
     * @param participantId The ID of the participant user for the One to One DM conversation.
  
  
  
  
     * @returns {Promise<GetEventsByParticipantIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getEventsByParticipantId(participantId, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      event_types: "eventTypes",
      "dm_event.fields": "dmEventFields",
      "media.fields": "mediaFields",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      eventTypes = [],
      dmEventFields = [],
      expansions = [],
      mediaFields = [],
      userFields = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/dm_conversations/with/{participant_id}/dm_events";
    path = path.replace(
      "{participant_id}",
      encodeURIComponent(String(participantId))
    );
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (eventTypes !== void 0 && eventTypes.length > 0) {
      params.append("event_types", eventTypes.join(","));
    }
    if (dmEventFields !== void 0 && dmEventFields.length > 0) {
      params.append("dm_event.fields", dmEventFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get DM events for a DM conversation
     * Retrieves direct message events for a specific conversation.
  
  
     * @param id The DM conversation ID.
  
  
  
  
     * @returns {Promise<GetEventsByConversationIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getEventsByConversationId(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      event_types: "eventTypes",
      "dm_event.fields": "dmEventFields",
      "media.fields": "mediaFields",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      eventTypes = [],
      dmEventFields = [],
      expansions = [],
      mediaFields = [],
      userFields = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/dm_conversations/{id}/dm_events";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (eventTypes !== void 0 && eventTypes.length > 0) {
      params.append("event_types", eventTypes.join(","));
    }
    if (dmEventFields !== void 0 && dmEventFields.length > 0) {
      params.append("dm_event.fields", dmEventFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get DM event by ID
     * Retrieves details of a specific direct message event by its ID.
  
  
     * @param eventId dm event id.
  
  
  
  
     * @returns {Promise<GetEventsByIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getEventsById(eventId, options = {}) {
    const paramMappings = {
      "dm_event.fields": "dmEventFields",
      "media.fields": "mediaFields",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      dmEventFields = [],
      expansions = [],
      mediaFields = [],
      userFields = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/dm_events/{event_id}";
    path = path.replace("{event_id}", encodeURIComponent(String(eventId)));
    const params = new URLSearchParams();
    if (dmEventFields !== void 0 && dmEventFields.length > 0) {
      params.append("dm_event.fields", dmEventFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Delete DM event
     * Deletes a specific direct message event by its ID, if owned by the authenticated user.
  
  
     * @param eventId The ID of the direct-message event to delete.
  
  
  
  
     * @returns {Promise<DeleteEventsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async deleteEvents(eventId) {
    let path = "/2/dm_events/{event_id}";
    path = path.replace("{event_id}", encodeURIComponent(String(eventId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.read", "dm.write"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create DM message by conversation ID
     * Sends a new direct message to a specific conversation by its ID.
  
  
     * @param dmConversationId The DM Conversation ID.
  
  
  
  
     * @returns {Promise<CreateByConversationIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createByConversationId(dmConversationId, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/dm_conversations/{dm_conversation_id}/messages";
    path = path.replace(
      "{dm_conversation_id}",
      encodeURIComponent(String(dmConversationId))
    );
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create DM conversation
     * Initiates a new direct message conversation with specified participants.
  
  
  
     * @returns {Promise<CreateConversationResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createConversation(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/dm_conversations";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/direct_messages/models.ts
var models_exports8 = {};

// src/posts/client.ts
var PostsClient = class {
  client;
  /**
     * Creates a new posts client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get 28-hour Post insights
     * Retrieves engagement metrics for specified Posts over the last 28 hours.
  
  
  
     * @param tweetIds List of PostIds for 28hr metrics.
  
  
  
     * @param granularity granularity of metrics response.
  
  
  
     * @param requestedMetrics request metrics for historical request.
  
  
  
     * @returns {Promise<GetInsights28hrResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getInsights28hr(tweetIds, granularity, requestedMetrics, options = {}) {
    const paramMappings = {
      "engagement.fields": "engagementFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      engagementFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/insights/28hr";
    const params = new URLSearchParams();
    if (tweetIds !== void 0 && tweetIds.length > 0) {
      params.append("tweet_ids", tweetIds.join(","));
    }
    if (granularity !== void 0) {
      params.append("granularity", String(granularity));
    }
    if (requestedMetrics !== void 0 && requestedMetrics.length > 0) {
      params.append("requested_metrics", requestedMetrics.join(","));
    }
    if (engagementFields !== void 0 && engagementFields.length > 0) {
      params.append("engagement.fields", engagementFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Reposts
     * Retrieves a list of Posts that repost a specific Post by its ID.
  
  
     * @param id A single Post ID.
  
  
  
  
     * @returns {Promise<GetRepostsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getReposts(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/{id}/retweets";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Search all Posts
     * Retrieves Posts from the full archive matching a search query.
  
  
  
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
  
  
  
     * @returns {Promise<SearchAllResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async searchAll(query, options = {}) {
    const paramMappings = {
      start_time: "startTime",
      end_time: "endTime",
      since_id: "sinceId",
      until_id: "untilId",
      max_results: "maxResults",
      next_token: "nextToken",
      pagination_token: "paginationToken",
      sort_order: "sortOrder",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      startTime = void 0,
      endTime = void 0,
      sinceId = void 0,
      untilId = void 0,
      maxResults = void 0,
      nextToken = void 0,
      paginationToken = void 0,
      sortOrder = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/search/all";
    const params = new URLSearchParams();
    if (query !== void 0) {
      params.append("query", String(query));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (sinceId !== void 0) {
      params.append("since_id", String(sinceId));
    }
    if (untilId !== void 0) {
      params.append("until_id", String(untilId));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (nextToken !== void 0) {
      params.append("next_token", String(nextToken));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (sortOrder !== void 0) {
      params.append("sort_order", String(sortOrder));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get historical Post insights
     * Retrieves historical engagement metrics for specified Posts within a defined time range.
  
  
  
     * @param tweetIds List of PostIds for historical metrics.
  
  
  
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
  
  
  
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
  
  
  
     * @param granularity granularity of metrics response.
  
  
  
     * @param requestedMetrics request metrics for historical request.
  
  
  
     * @returns {Promise<GetInsightsHistoricalResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getInsightsHistorical(tweetIds, endTime, startTime, granularity, requestedMetrics, options = {}) {
    const paramMappings = {
      "engagement.fields": "engagementFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      engagementFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/insights/historical";
    const params = new URLSearchParams();
    if (tweetIds !== void 0 && tweetIds.length > 0) {
      params.append("tweet_ids", tweetIds.join(","));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (granularity !== void 0) {
      params.append("granularity", String(granularity));
    }
    if (requestedMetrics !== void 0 && requestedMetrics.length > 0) {
      params.append("requested_metrics", requestedMetrics.join(","));
    }
    if (engagementFields !== void 0 && engagementFields.length > 0) {
      params.append("engagement.fields", engagementFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Post by ID
     * Retrieves details of a specific Post by its ID.
  
  
     * @param id A single Post ID.
  
  
  
  
     * @returns {Promise<GetByIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getById(id, options = {}) {
    const paramMappings = {
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Delete Post
     * Deletes a specific Post by its ID, if owned by the authenticated user.
  
  
     * @param id The ID of the Post to be deleted.
  
  
  
  
     * @returns {Promise<DeleteResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async delete(id) {
    let path = "/2/tweets/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "tweet.write", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Post analytics
     * Retrieves analytics data for specified Posts within a defined time range.
  
  
  
     * @param ids A comma separated list of Post IDs. Up to 100 are allowed in a single request.
  
  
  
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
  
  
  
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
  
  
  
     * @param granularity The granularity for the search counts results.
  
  
  
     * @returns {Promise<GetAnalyticsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getAnalytics(ids, endTime, startTime, granularity, options = {}) {
    const paramMappings = {
      "analytics.fields": "analyticsFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      analyticsFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/analytics";
    const params = new URLSearchParams();
    if (ids !== void 0 && ids.length > 0) {
      params.append("ids", ids.join(","));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (granularity !== void 0) {
      params.append("granularity", String(granularity));
    }
    if (analyticsFields !== void 0 && analyticsFields.length > 0) {
      params.append("analytics.fields", analyticsFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Posts by IDs
     * Retrieves details of multiple Posts by their IDs.
  
  
  
     * @param ids A comma separated list of Post IDs. Up to 100 are allowed in a single request.
  
  
  
     * @returns {Promise<GetByIdsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getByIds(ids, options = {}) {
    const paramMappings = {
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets";
    const params = new URLSearchParams();
    if (ids !== void 0 && ids.length > 0) {
      params.append("ids", ids.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create or Edit Post
     * Creates a new Post for the authenticated user, or edits an existing Post when edit_options are provided.
  
  
  
     * @param body Request body
  
     * @returns {Promise<CreateResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async create(body) {
    let path = "/2/tweets";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: JSON.stringify(body || {}),
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "tweet.write", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get count of recent Posts
     * Retrieves the count of Posts from the last 7 days matching a search query.
  
  
  
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
  
  
  
     * @returns {Promise<GetCountsRecentResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getCountsRecent(query, options = {}) {
    const paramMappings = {
      start_time: "startTime",
      end_time: "endTime",
      since_id: "sinceId",
      until_id: "untilId",
      next_token: "nextToken",
      pagination_token: "paginationToken",
      "search_count.fields": "searchCountFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      startTime = void 0,
      endTime = void 0,
      sinceId = void 0,
      untilId = void 0,
      nextToken = void 0,
      paginationToken = void 0,
      granularity = void 0,
      searchCountFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/counts/recent";
    const params = new URLSearchParams();
    if (query !== void 0) {
      params.append("query", String(query));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (sinceId !== void 0) {
      params.append("since_id", String(sinceId));
    }
    if (untilId !== void 0) {
      params.append("until_id", String(untilId));
    }
    if (nextToken !== void 0) {
      params.append("next_token", String(nextToken));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (granularity !== void 0) {
      params.append("granularity", String(granularity));
    }
    if (searchCountFields !== void 0 && searchCountFields.length > 0) {
      params.append("search_count.fields", searchCountFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get count of all Posts
     * Retrieves the count of Posts matching a search query from the full archive.
  
  
  
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
  
  
  
     * @returns {Promise<GetCountsAllResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getCountsAll(query, options = {}) {
    const paramMappings = {
      start_time: "startTime",
      end_time: "endTime",
      since_id: "sinceId",
      until_id: "untilId",
      next_token: "nextToken",
      pagination_token: "paginationToken",
      "search_count.fields": "searchCountFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      startTime = void 0,
      endTime = void 0,
      sinceId = void 0,
      untilId = void 0,
      nextToken = void 0,
      paginationToken = void 0,
      granularity = void 0,
      searchCountFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/counts/all";
    const params = new URLSearchParams();
    if (query !== void 0) {
      params.append("query", String(query));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (sinceId !== void 0) {
      params.append("since_id", String(sinceId));
    }
    if (untilId !== void 0) {
      params.append("until_id", String(untilId));
    }
    if (nextToken !== void 0) {
      params.append("next_token", String(nextToken));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (granularity !== void 0) {
      params.append("granularity", String(granularity));
    }
    if (searchCountFields !== void 0 && searchCountFields.length > 0) {
      params.append("search_count.fields", searchCountFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Search recent Posts
     * Retrieves Posts from the last 7 days matching a search query.
  
  
  
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
  
  
  
     * @returns {Promise<SearchRecentResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async searchRecent(query, options = {}) {
    const paramMappings = {
      start_time: "startTime",
      end_time: "endTime",
      since_id: "sinceId",
      until_id: "untilId",
      max_results: "maxResults",
      next_token: "nextToken",
      pagination_token: "paginationToken",
      sort_order: "sortOrder",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      startTime = void 0,
      endTime = void 0,
      sinceId = void 0,
      untilId = void 0,
      maxResults = void 0,
      nextToken = void 0,
      paginationToken = void 0,
      sortOrder = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/search/recent";
    const params = new URLSearchParams();
    if (query !== void 0) {
      params.append("query", String(query));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (sinceId !== void 0) {
      params.append("since_id", String(sinceId));
    }
    if (untilId !== void 0) {
      params.append("until_id", String(untilId));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (nextToken !== void 0) {
      params.append("next_token", String(nextToken));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (sortOrder !== void 0) {
      params.append("sort_order", String(sortOrder));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Hide reply
     * Hides or unhides a reply to a conversation owned by the authenticated user.
  
  
     * @param tweetId The ID of the reply that you want to hide or unhide.
  
  
  
  
     * @returns {Promise<HideReplyResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async hideReply(tweetId, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/{tweet_id}/hidden";
    path = path.replace("{tweet_id}", encodeURIComponent(String(tweetId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.moderate.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "PUT",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Reposted by
     * Retrieves a list of Users who reposted a specific Post by its ID.
  
  
     * @param id A single Post ID.
  
  
  
  
     * @returns {Promise<GetRepostedByResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getRepostedBy(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/{id}/retweeted_by";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Quoted Posts
     * Retrieves a list of Posts that quote a specific Post by its ID.
  
  
     * @param id A single Post ID.
  
  
  
  
     * @returns {Promise<GetQuotedResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getQuoted(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      exclude = [],
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/{id}/quote_tweets";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (exclude !== void 0 && exclude.length > 0) {
      params.append("exclude", exclude.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Liking Users
     * Retrieves a list of Users who liked a specific Post by its ID.
  
  
     * @param id A single Post ID.
  
  
  
  
     * @returns {Promise<GetLikingUsersResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getLikingUsers(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/{id}/liking_users";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["like.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/posts/models.ts
var models_exports9 = {};

// src/lists/client.ts
var ListsClient = class {
  client;
  /**
     * Creates a new lists client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get List members
     * Retrieves a list of Users who are members of a specific List by its ID.
  
  
     * @param id The ID of the List.
  
  
  
  
     * @returns {Promise<GetMembersResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getMembers(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/lists/{id}/members";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["list.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Add List member
     * Adds a User to a specific List by its ID.
  
  
     * @param id The ID of the List for which to add a member.
  
  
  
  
     * @returns {Promise<AddMemberResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async addMember(id, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/lists/{id}/members";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["list.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get List followers
     * Retrieves a list of Users who follow a specific List by its ID.
  
  
     * @param id The ID of the List.
  
  
  
  
     * @returns {Promise<GetFollowersResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getFollowers(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/lists/{id}/followers";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["list.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get List Posts
     * Retrieves a list of Posts associated with a specific List by its ID.
  
  
     * @param id The ID of the List.
  
  
  
  
     * @returns {Promise<GetPostsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getPosts(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/lists/{id}/tweets";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["list.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Remove List member
     * Removes a User from a specific List by its ID and the User’s ID.
  
  
     * @param id The ID of the List to remove a member.
  
  
  
     * @param userId The ID of User that will be removed from the List.
  
  
  
  
     * @returns {Promise<RemoveMemberByUserIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async removeMemberByUserId(id, userId) {
    let path = "/2/lists/{id}/members/{user_id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    path = path.replace("{user_id}", encodeURIComponent(String(userId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["list.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get List by ID
     * Retrieves details of a specific List by its ID.
  
  
     * @param id The ID of the List.
  
  
  
  
     * @returns {Promise<GetByIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getById(id, options = {}) {
    const paramMappings = {
      "list.fields": "listFields",
      "user.fields": "userFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      listFields = [],
      expansions = [],
      userFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/lists/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (listFields !== void 0 && listFields.length > 0) {
      params.append("list.fields", listFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["list.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Update List
     * Updates the details of a specific List owned by the authenticated user by its ID.
  
  
     * @param id The ID of the List to modify.
  
  
  
  
     * @returns {Promise<UpdateResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async update(id, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/lists/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["list.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "PUT",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Delete List
     * Deletes a specific List owned by the authenticated user by its ID.
  
  
     * @param id The ID of the List to delete.
  
  
  
  
     * @returns {Promise<DeleteResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async delete(id) {
    let path = "/2/lists/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["list.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create List
     * Creates a new List for the authenticated user.
  
  
  
     * @returns {Promise<CreateResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async create(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/lists";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: [
            "list.read",
            "list.write",
            "tweet.read",
            "users.read"
          ]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/lists/models.ts
var models_exports10 = {};

// src/community_notes/client.ts
var CommunityNotesClient = class {
  client;
  /**
     * Creates a new community notes client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Delete a Community Note
     * Deletes a community note.
  
  
     * @param id The community note id to delete.
  
  
  
  
     * @returns {Promise<DeleteResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async delete(id) {
    let path = "/2/notes/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.write"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Evaluate a Community Note
     * Endpoint to evaluate a community note.
  
  
  
     * @returns {Promise<EvaluateResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async evaluate(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/evaluate_note";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.write"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Search for Community Notes Written
     * Returns all the community notes written by the user.
  
  
  
     * @param testMode If true, return the notes the caller wrote for the test. If false, return the notes the caller wrote on the product.
  
  
  
     * @returns {Promise<SearchWrittenResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async searchWritten(testMode, options = {}) {
    const paramMappings = {
      pagination_token: "paginationToken",
      max_results: "maxResults",
      "note.fields": "noteFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      paginationToken = void 0,
      maxResults = void 0,
      noteFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/notes/search/notes_written";
    const params = new URLSearchParams();
    if (testMode !== void 0) {
      params.append("test_mode", String(testMode));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (noteFields !== void 0 && noteFields.length > 0) {
      params.append("note.fields", noteFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create a Community Note
     * Creates a community note endpoint for LLM use case.
  
  
  
     * @returns {Promise<CreateResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async create(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/notes";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.write"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Search for Posts Eligible for Community Notes
     * Returns all the posts that are eligible for community notes.
  
  
  
     * @param testMode If true, return a list of posts that are for the test. If false, return a list of posts that the bots can write proposed notes on the product.
  
  
  
     * @returns {Promise<SearchEligiblePostsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async searchEligiblePosts(testMode, options = {}) {
    const paramMappings = {
      pagination_token: "paginationToken",
      max_results: "maxResults",
      post_selection: "postSelection",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      paginationToken = void 0,
      maxResults = void 0,
      postSelection = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/notes/search/posts_eligible_for_notes";
    const params = new URLSearchParams();
    if (testMode !== void 0) {
      params.append("test_mode", String(testMode));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (postSelection !== void 0) {
      params.append("post_selection", String(postSelection));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/community_notes/models.ts
var models_exports11 = {};

// src/general/client.ts
var GeneralClient = class {
  client;
  /**
     * Creates a new general client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get OpenAPI Spec.
     * Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)
  
  
  
     * @returns {Promise<GetOpenApiSpecResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getOpenApiSpec() {
    let path = "/2/openapi.json";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/general/models.ts
var models_exports12 = {};

// src/webhooks/client.ts
var WebhooksClient = class {
  client;
  /**
     * Creates a new webhooks client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get webhook
     * Get a list of webhook configs associated with a client app.
  
  
  
     * @returns {Promise<GetResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async get(options = {}) {
    const paramMappings = {
      "webhook_config.fields": "webhookConfigFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      webhookConfigFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/webhooks";
    const params = new URLSearchParams();
    if (webhookConfigFields !== void 0 && webhookConfigFields.length > 0) {
      params.append("webhook_config.fields", webhookConfigFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create webhook
     * Creates a new webhook configuration.
  
  
  
     * @returns {Promise<CreateResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async create(options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/webhooks";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Validate webhook
     * Triggers a CRC check for a given webhook.
  
  
     * @param webhookId The ID of the webhook to check.
  
  
  
  
     * @returns {Promise<ValidateResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async validate(webhookId) {
    let path = "/2/webhooks/{webhook_id}";
    path = path.replace("{webhook_id}", encodeURIComponent(String(webhookId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "PUT",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Delete webhook
     * Deletes an existing webhook configuration.
  
  
     * @param webhookId The ID of the webhook to delete.
  
  
  
  
     * @returns {Promise<DeleteResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async delete(webhookId) {
    let path = "/2/webhooks/{webhook_id}";
    path = path.replace("{webhook_id}", encodeURIComponent(String(webhookId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create stream link
     * Creates a link to deliver FilteredStream events to the given webhook.
  
  
     * @param webhookId The webhook ID to link to your FilteredStream ruleset.
  
  
  
  
     * @returns {Promise<CreateStreamLinkResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createStreamLink(webhookId, options = {}) {
    const paramMappings = {
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      tweetFields = void 0,
      expansions = void 0,
      mediaFields = void 0,
      pollFields = void 0,
      userFields = void 0,
      placeFields = void 0,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/search/webhooks/{webhook_id}";
    path = path.replace("{webhook_id}", encodeURIComponent(String(webhookId)));
    const params = new URLSearchParams();
    if (tweetFields !== void 0) {
      params.append("tweet.fields", String(tweetFields));
    }
    if (expansions !== void 0) {
      params.append("expansions", String(expansions));
    }
    if (mediaFields !== void 0) {
      params.append("media.fields", String(mediaFields));
    }
    if (pollFields !== void 0) {
      params.append("poll.fields", String(pollFields));
    }
    if (userFields !== void 0) {
      params.append("user.fields", String(userFields));
    }
    if (placeFields !== void 0) {
      params.append("place.fields", String(placeFields));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Delete stream link
     * Deletes a link from FilteredStream events to the given webhook.
  
  
     * @param webhookId The webhook ID to link to your FilteredStream ruleset.
  
  
  
  
     * @returns {Promise<DeleteStreamLinkResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async deleteStreamLink(webhookId) {
    let path = "/2/tweets/search/webhooks/{webhook_id}";
    path = path.replace("{webhook_id}", encodeURIComponent(String(webhookId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get stream links
     * Get a list of webhook links associated with a filtered stream ruleset.
  
  
  
     * @returns {Promise<GetStreamLinksResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getStreamLinks() {
    let path = "/2/tweets/search/webhooks";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/webhooks/models.ts
var models_exports13 = {};

// src/users/client.ts
var UsersClient = class {
  client;
  /**
     * Creates a new users client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get Users by usernames
     * Retrieves details of multiple Users by their usernames.
  
  
  
     * @param usernames A list of usernames, comma-separated.
  
  
  
     * @returns {Promise<GetByUsernamesResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getByUsernames(usernames, options = {}) {
    const paramMappings = {
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/by";
    const params = new URLSearchParams();
    if (usernames !== void 0 && usernames.length > 0) {
      params.append("usernames", usernames.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get List memberships
     * Retrieves a list of Lists that a specific User is a member of by their ID.
  
  
     * @param id The ID of the User to lookup.
  
  
  
  
     * @returns {Promise<GetListMembershipsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getListMemberships(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "list.fields": "listFields",
      "user.fields": "userFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      listFields = [],
      expansions = [],
      userFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/list_memberships";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (listFields !== void 0 && listFields.length > 0) {
      params.append("list.fields", listFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["list.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Unfollow User
     * Causes the authenticated user to unfollow a specific user by their ID.
  
  
     * @param sourceUserId The ID of the authenticated source User that is requesting to unfollow the target User.
  
  
  
     * @param targetUserId The ID of the User that the source User is requesting to unfollow.
  
  
  
  
     * @returns {Promise<UnfollowUserResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async unfollowUser(sourceUserId, targetUserId) {
    let path = "/2/users/{source_user_id}/following/{target_user_id}";
    path = path.replace(
      "{source_user_id}",
      encodeURIComponent(String(sourceUserId))
    );
    path = path.replace(
      "{target_user_id}",
      encodeURIComponent(String(targetUserId))
    );
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["follows.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Unfollow List
     * Causes the authenticated user to unfollow a specific List by its ID.
  
  
     * @param id The ID of the authenticated source User that will unfollow the List.
  
  
  
     * @param listId The ID of the List to unfollow.
  
  
  
  
     * @returns {Promise<UnfollowListResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async unfollowList(id, listId) {
    let path = "/2/users/{id}/followed_lists/{list_id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    path = path.replace("{list_id}", encodeURIComponent(String(listId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["list.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Users by IDs
     * Retrieves details of multiple Users by their IDs.
  
  
  
     * @param ids A list of User IDs, comma-separated. You can specify up to 100 IDs.
  
  
  
     * @returns {Promise<GetByIdsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getByIds(ids, options = {}) {
    const paramMappings = {
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users";
    const params = new URLSearchParams();
    if (ids !== void 0 && ids.length > 0) {
      params.append("ids", ids.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Like Post
     * Causes the authenticated user to Like a specific Post by its ID.
  
  
     * @param id The ID of the authenticated source User that is requesting to like the Post.
  
  
  
  
     * @returns {Promise<LikePostResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async likePost(id, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/likes";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["like.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Block DMs
     * Blocks direct messages to or from a specific User by their ID for the authenticated user.
  
  
     * @param id The ID of the target User that the authenticated user requesting to block dms for.
  
  
  
  
     * @returns {Promise<BlockDmsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async blockDms(id) {
    let path = "/2/users/{id}/dm/block";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Posts
     * Retrieves a list of posts authored by a specific User by their ID.
  
  
     * @param id The ID of the User to lookup.
  
  
  
  
     * @returns {Promise<GetPostsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getPosts(id, options = {}) {
    const paramMappings = {
      since_id: "sinceId",
      until_id: "untilId",
      max_results: "maxResults",
      pagination_token: "paginationToken",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      sinceId = void 0,
      untilId = void 0,
      maxResults = void 0,
      paginationToken = void 0,
      exclude = [],
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/tweets";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (sinceId !== void 0) {
      params.append("since_id", String(sinceId));
    }
    if (untilId !== void 0) {
      params.append("until_id", String(untilId));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (exclude !== void 0 && exclude.length > 0) {
      params.append("exclude", exclude.join(","));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Bookmarks by folder ID
     * Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.
  
  
     * @param id The ID of the authenticated source User for whom to return results.
  
  
  
     * @param folderId The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for.
  
  
  
  
     * @returns {Promise<GetBookmarksByFolderIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getBookmarksByFolderId(id, folderId) {
    let path = "/2/users/{id}/bookmarks/folders/{folder_id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    path = path.replace("{folder_id}", encodeURIComponent(String(folderId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["bookmark.read", "tweet.read", "users.read"]
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get muting
     * Retrieves a list of Users muted by the authenticated user.
  
  
     * @param id The ID of the authenticated source User for whom to return results.
  
  
  
  
     * @returns {Promise<GetMutingResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getMuting(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/muting";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["mute.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Mute User
     * Causes the authenticated user to mute a specific User by their ID.
  
  
     * @param id The ID of the authenticated source User that is requesting to mute the target User.
  
  
  
  
     * @returns {Promise<MuteUserResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async muteUser(id, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/muting";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["mute.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get owned Lists
     * Retrieves a list of Lists owned by a specific User by their ID.
  
  
     * @param id The ID of the User to lookup.
  
  
  
  
     * @returns {Promise<GetOwnedListsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getOwnedLists(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "list.fields": "listFields",
      "user.fields": "userFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      listFields = [],
      expansions = [],
      userFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/owned_lists";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (listFields !== void 0 && listFields.length > 0) {
      params.append("list.fields", listFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["list.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Unpin List
     * Causes the authenticated user to unpin a specific List by its ID.
  
  
     * @param id The ID of the authenticated source User for whom to return results.
  
  
  
     * @param listId The ID of the List to unpin.
  
  
  
  
     * @returns {Promise<UnpinListResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async unpinList(id, listId) {
    let path = "/2/users/{id}/pinned_lists/{list_id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    path = path.replace("{list_id}", encodeURIComponent(String(listId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["list.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get User by username
     * Retrieves details of a specific User by their username.
  
  
     * @param username A username.
  
  
  
  
     * @returns {Promise<GetByUsernameResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getByUsername(username, options = {}) {
    const paramMappings = {
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/by/username/{username}";
    path = path.replace("{username}", encodeURIComponent(String(username)));
    const params = new URLSearchParams();
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get blocking
     * Retrieves a list of Users blocked by the specified User ID.
  
  
     * @param id The ID of the authenticated source User for whom to return results.
  
  
  
  
     * @returns {Promise<GetBlockingResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getBlocking(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/blocking";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["block.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get liked Posts
     * Retrieves a list of Posts liked by a specific User by their ID.
  
  
     * @param id The ID of the User to lookup.
  
  
  
  
     * @returns {Promise<GetLikedPostsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getLikedPosts(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/liked_tweets";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["like.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Unlike Post
     * Causes the authenticated user to Unlike a specific Post by its ID.
  
  
     * @param id The ID of the authenticated source User that is requesting to unlike the Post.
  
  
  
     * @param tweetId The ID of the Post that the User is requesting to unlike.
  
  
  
  
     * @returns {Promise<UnlikePostResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async unlikePost(id, tweetId) {
    let path = "/2/users/{id}/likes/{tweet_id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    path = path.replace("{tweet_id}", encodeURIComponent(String(tweetId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["like.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get followed Lists
     * Retrieves a list of Lists followed by a specific User by their ID.
  
  
     * @param id The ID of the User to lookup.
  
  
  
  
     * @returns {Promise<GetFollowedListsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getFollowedLists(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "list.fields": "listFields",
      "user.fields": "userFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      listFields = [],
      expansions = [],
      userFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/followed_lists";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (listFields !== void 0 && listFields.length > 0) {
      params.append("list.fields", listFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["list.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Follow List
     * Causes the authenticated user to follow a specific List by its ID.
  
  
     * @param id The ID of the authenticated source User that will follow the List.
  
  
  
  
     * @returns {Promise<FollowListResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async followList(id, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/followed_lists";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["list.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Timeline
     * Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.
  
  
     * @param id The ID of the authenticated source User to list Reverse Chronological Timeline Posts of.
  
  
  
  
     * @returns {Promise<GetTimelineResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getTimeline(id, options = {}) {
    const paramMappings = {
      since_id: "sinceId",
      until_id: "untilId",
      max_results: "maxResults",
      pagination_token: "paginationToken",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      sinceId = void 0,
      untilId = void 0,
      maxResults = void 0,
      paginationToken = void 0,
      exclude = [],
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/timelines/reverse_chronological";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (sinceId !== void 0) {
      params.append("since_id", String(sinceId));
    }
    if (untilId !== void 0) {
      params.append("until_id", String(untilId));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (exclude !== void 0 && exclude.length > 0) {
      params.append("exclude", exclude.join(","));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get pinned Lists
     * Retrieves a list of Lists pinned by the authenticated user.
  
  
     * @param id The ID of the authenticated source User for whom to return results.
  
  
  
  
     * @returns {Promise<GetPinnedListsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getPinnedLists(id, options = {}) {
    const paramMappings = {
      "list.fields": "listFields",
      "user.fields": "userFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      listFields = [],
      expansions = [],
      userFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/pinned_lists";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (listFields !== void 0 && listFields.length > 0) {
      params.append("list.fields", listFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["list.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Pin List
     * Causes the authenticated user to pin a specific List by its ID.
  
  
     * @param id The ID of the authenticated source User that will pin the List.
  
  
  
  
     * @param body Request body
  
     * @returns {Promise<PinListResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async pinList(id, body) {
    let path = "/2/users/{id}/pinned_lists";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: JSON.stringify(body || {}),
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["list.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Reposts of me
     * Retrieves a list of Posts that repost content from the authenticated user.
  
  
  
     * @returns {Promise<GetRepostsOfMeResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getRepostsOfMe(options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/reposts_of_me";
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["timeline.read", "tweet.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get following
     * Retrieves a list of Users followed by a specific User by their ID.
  
  
     * @param id The ID of the User to lookup.
  
  
  
  
     * @returns {Promise<GetFollowingResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getFollowing(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/following";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["follows.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Follow User
     * Causes the authenticated user to follow a specific user by their ID.
  
  
     * @param id The ID of the authenticated source User that is requesting to follow the target User.
  
  
  
  
     * @returns {Promise<FollowUserResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async followUser(id, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/following";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["follows.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Unblock DMs
     * Unblocks direct messages to or from a specific User by their ID for the authenticated user.
  
  
     * @param id The ID of the target User that the authenticated user requesting to unblock dms for.
  
  
  
  
     * @returns {Promise<UnblockDmsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async unblockDms(id) {
    let path = "/2/users/{id}/dm/unblock";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["dm.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get mentions
     * Retrieves a list of Posts that mention a specific User by their ID.
  
  
     * @param id The ID of the User to lookup.
  
  
  
  
     * @returns {Promise<GetMentionsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getMentions(id, options = {}) {
    const paramMappings = {
      since_id: "sinceId",
      until_id: "untilId",
      max_results: "maxResults",
      pagination_token: "paginationToken",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      sinceId = void 0,
      untilId = void 0,
      maxResults = void 0,
      paginationToken = void 0,
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/mentions";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (sinceId !== void 0) {
      params.append("since_id", String(sinceId));
    }
    if (untilId !== void 0) {
      params.append("until_id", String(untilId));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Bookmark folders
     * Retrieves a list of Bookmark folders created by the authenticated user.
  
  
     * @param id The ID of the authenticated source User for whom to return results.
  
  
  
  
     * @returns {Promise<GetBookmarkFoldersResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getBookmarkFolders(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/bookmarks/folders";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["bookmark.read", "users.read"]
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Unrepost Post
     * Causes the authenticated user to unrepost a specific Post by its ID.
  
  
     * @param id The ID of the authenticated source User that is requesting to repost the Post.
  
  
  
     * @param sourceTweetId The ID of the Post that the User is requesting to unretweet.
  
  
  
  
     * @returns {Promise<UnrepostPostResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async unrepostPost(id, sourceTweetId) {
    let path = "/2/users/{id}/retweets/{source_tweet_id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    path = path.replace(
      "{source_tweet_id}",
      encodeURIComponent(String(sourceTweetId))
    );
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "tweet.write", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Delete Bookmark
     * Removes a Post from the authenticated user’s Bookmarks by its ID.
  
  
     * @param id The ID of the authenticated source User whose bookmark is to be removed.
  
  
  
     * @param tweetId The ID of the Post that the source User is removing from bookmarks.
  
  
  
  
     * @returns {Promise<DeleteBookmarkResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async deleteBookmark(id, tweetId) {
    let path = "/2/users/{id}/bookmarks/{tweet_id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    path = path.replace("{tweet_id}", encodeURIComponent(String(tweetId)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["bookmark.write", "tweet.read", "users.read"]
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Repost Post
     * Causes the authenticated user to repost a specific Post by its ID.
  
  
     * @param id The ID of the authenticated source User that is requesting to repost the Post.
  
  
  
  
     * @returns {Promise<RepostPostResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async repostPost(id, options = {}) {
    const normalizedOptions = options || {};
    const {
      body,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/retweets";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: body ? JSON.stringify(body) : void 0,
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "tweet.write", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Search Users
     * Retrieves a list of Users matching a search query.
  
  
  
     * @param query TThe the query string by which to query for users.
  
  
  
     * @returns {Promise<SearchResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async search(query, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      next_token: "nextToken",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      nextToken = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/search";
    const params = new URLSearchParams();
    if (query !== void 0) {
      params.append("query", String(query));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (nextToken !== void 0) {
      params.append("next_token", String(nextToken));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get User by ID
     * Retrieves details of a specific User by their ID.
  
  
     * @param id The ID of the User to lookup.
  
  
  
  
     * @returns {Promise<GetByIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getById(id, options = {}) {
    const paramMappings = {
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Bookmarks
     * Retrieves a list of Posts bookmarked by the authenticated user.
  
  
     * @param id The ID of the authenticated source User for whom to return results.
  
  
  
  
     * @returns {Promise<GetBookmarksResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getBookmarks(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/bookmarks";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["bookmark.read", "tweet.read", "users.read"]
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create Bookmark
     * Adds a post to the authenticated user’s bookmarks.
  
  
     * @param id The ID of the authenticated source User for whom to add bookmarks.
  
  
  
  
     * @param body Request body
  
     * @returns {Promise<CreateBookmarkResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createBookmark(id, body) {
    let path = "/2/users/{id}/bookmarks";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: JSON.stringify(body || {}),
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["bookmark.write", "tweet.read", "users.read"]
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get followers
     * Retrieves a list of Users who follow a specific User by their ID.
  
  
     * @param id The ID of the User to lookup.
  
  
  
  
     * @returns {Promise<GetFollowersResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getFollowers(id, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      paginationToken = void 0,
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/{id}/followers";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["follows.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get my User
     * Retrieves details of the authenticated user.
  
  
  
     * @returns {Promise<GetMeResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getMe(options = {}) {
    const paramMappings = {
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      userFields = [],
      expansions = [],
      tweetFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/me";
    const params = new URLSearchParams();
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Unmute User
     * Causes the authenticated user to unmute a specific user by their ID.
  
  
     * @param sourceUserId The ID of the authenticated source User that is requesting to unmute the target User.
  
  
  
     * @param targetUserId The ID of the User that the source User is requesting to unmute.
  
  
  
  
     * @returns {Promise<UnmuteUserResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async unmuteUser(sourceUserId, targetUserId) {
    let path = "/2/users/{source_user_id}/muting/{target_user_id}";
    path = path.replace(
      "{source_user_id}",
      encodeURIComponent(String(sourceUserId))
    );
    path = path.replace(
      "{target_user_id}",
      encodeURIComponent(String(targetUserId))
    );
    const params = new URLSearchParams();
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["mute.write", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "DELETE",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/users/models.ts
var models_exports14 = {};

// src/communities/client.ts
var CommunitiesClient = class {
  client;
  /**
     * Creates a new communities client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get Community by ID
     * Retrieves details of a specific Community by its ID.
  
  
     * @param id The ID of the Community.
  
  
  
  
     * @returns {Promise<GetByIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getById(id, options = {}) {
    const paramMappings = {
      "community.fields": "communityFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      communityFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/communities/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (communityFields !== void 0 && communityFields.length > 0) {
      params.append("community.fields", communityFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        },
        {
          OAuth2UserToken: ["list.read", "tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Search Communities
     * Retrieves a list of Communities matching the specified search query.
  
  
  
     * @param query Query to search communities.
  
  
  
     * @returns {Promise<SearchResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async search(query, options = {}) {
    const paramMappings = {
      max_results: "maxResults",
      next_token: "nextToken",
      pagination_token: "paginationToken",
      "community.fields": "communityFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      maxResults = void 0,
      nextToken = void 0,
      paginationToken = void 0,
      communityFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/communities/search";
    const params = new URLSearchParams();
    if (query !== void 0) {
      params.append("query", String(query));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (nextToken !== void 0) {
      params.append("next_token", String(nextToken));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    if (communityFields !== void 0 && communityFields.length > 0) {
      params.append("community.fields", communityFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          OAuth2UserToken: ["tweet.read", "users.read"]
        },
        {
          UserToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/communities/models.ts
var models_exports15 = {};

// src/stream/event_driven_stream.ts
var StreamEvent = {
  Data: "data",
  // When JSON data arrives
  KeepAlive: "keepAlive",
  // 20-second heartbeat (newline character)
  Error: "error",
  // HTTP errors, ConnectionException, operational-disconnect
  Close: "close"
  // When stream ends
};
var EventDrivenStream = class {
  webStream = null;
  reader = null;
  decoder;
  isConnected = false;
  isClosed = false;
  buffer = "";
  eventListeners = /* @__PURE__ */ new Map();
  autoReconnect = false;
  reconnectAttempts = 0;
  maxReconnectAttempts = 5;
  reconnectDelay = 1e3;
  constructor() {
    this.decoder = new TextDecoder();
    this.setupEventListeners();
  }
  /**
   * Initialize the stream with a Web ReadableStream
   */
  async connect(webStream) {
    if (this.isConnected) {
      throw new Error("Stream is already connected");
    }
    this.webStream = webStream;
    this.isConnected = true;
    this.isClosed = false;
    this.reconnectAttempts = 0;
    this.emit(StreamEvent.Data, { message: "Stream connected" });
    this.startReading();
  }
  /**
   * Start reading from the stream
   */
  async startReading() {
    if (!this.webStream || !this.isConnected) {
      return;
    }
    this.reader = this.webStream.getReader();
    try {
      while (this.isConnected && !this.isClosed) {
        const { done, value } = await this.reader.read();
        if (done) {
          this.handleConnectionClosed();
          break;
        }
        if (value) {
          await this.processChunk(value);
        }
      }
    } catch (error) {
      this.handleConnectionError(error);
    } finally {
      this.cleanup();
    }
  }
  /**
   * Process incoming data chunks
   */
  async processChunk(value) {
    const chunk = this.decoder.decode(value, { stream: true });
    this.buffer += chunk;
    let boundary;
    while ((boundary = this.buffer.indexOf("\n")) !== -1) {
      const line = this.buffer.substring(0, boundary);
      this.buffer = this.buffer.substring(boundary + 1);
      if (line.trim()) {
        try {
          const data = JSON.parse(line);
          if (this.isKeepAlive(data)) {
            this.emit(StreamEvent.KeepAlive, { data });
            continue;
          }
          this.emit(StreamEvent.Data, data);
        } catch (parseError) {
          console.warn("Skipping invalid JSON:", line.substring(0, 100));
        }
      }
    }
  }
  /**
   * Check if data is a keep-alive signal (20-second heartbeat)
   * Twitter sends newline characters every 20 seconds to prevent timeouts
   */
  isKeepAlive(data) {
    return !data.data && !data.includes && !data.matching_rules && !data.errors;
  }
  /**
   * Handle connection errors
   */
  handleConnectionError(error) {
    this.isConnected = false;
    this.emit(StreamEvent.Error, { error });
    if (this.autoReconnect && this.reconnectAttempts < this.maxReconnectAttempts) {
      this.attemptReconnect();
    }
  }
  /**
   * Handle connection closed
   */
  handleConnectionClosed() {
    this.isConnected = false;
    this.emit(StreamEvent.Close, { message: "Connection closed" });
  }
  /**
   * Attempt to reconnect
   */
  async attemptReconnect() {
    this.reconnectAttempts++;
    this.emit(StreamEvent.Data, {
      message: `Reconnect attempt ${this.reconnectAttempts}/${this.maxReconnectAttempts}`
    });
    await new Promise(
      (resolve) => setTimeout(resolve, this.reconnectDelay * this.reconnectAttempts)
    );
    try {
      this.emit(StreamEvent.Error, {
        error: new Error("Reconnect not implemented in this example")
      });
    } catch (error) {
      this.emit(StreamEvent.Error, { error });
    }
  }
  /**
   * Clean up resources
   */
  cleanup() {
    if (this.reader) {
      try {
        this.reader.releaseLock();
      } catch (error) {
        console.debug("Reader lock already released or error:", error);
      }
      this.reader = null;
    }
    this.buffer = "";
  }
  /**
   * Close the stream
   */
  close() {
    this.isClosed = true;
    this.isConnected = false;
    this.cleanup();
    this.emit(StreamEvent.Close, { message: "Stream closed by user" });
  }
  /**
   * Add event listener
   */
  on(event, listener) {
    if (!this.eventListeners.has(event)) {
      this.eventListeners.set(event, []);
    }
    this.eventListeners.get(event).push(listener);
    return this;
  }
  /**
   * Remove event listener
   */
  off(event, listener) {
    const listeners = this.eventListeners.get(event);
    if (listeners) {
      const index = listeners.indexOf(listener);
      if (index > -1) {
        listeners.splice(index, 1);
      }
    }
    return this;
  }
  /**
   * Emit event to listeners
   */
  emit(event, data) {
    const listeners = this.eventListeners.get(event);
    if (listeners) {
      listeners.forEach((listener) => {
        try {
          listener(data);
        } catch (error) {
          console.error(`Error in ${event} listener:`, error);
        }
      });
    }
  }
  /**
   * Setup default event listeners
   */
  setupEventListeners() {
    this.on(StreamEvent.Error, (eventData) => {
      console.error("Stream error:", eventData.error);
    });
  }
  /**
   * Enable/disable auto-reconnect
   */
  set autoReconnectEnabled(enabled) {
    this.autoReconnect = enabled;
  }
  get autoReconnectEnabled() {
    return this.autoReconnect;
  }
  /**
   * Set max reconnect attempts
   */
  set maxReconnectAttemptsCount(count) {
    this.maxReconnectAttempts = count;
  }
  get maxReconnectAttemptsCount() {
    return this.maxReconnectAttempts;
  }
  /**
   * Async iterator for tweets
   */
  async *[Symbol.asyncIterator]() {
    const dataQueue = [];
    let isComplete = false;
    let hasError = false;
    let error = null;
    const dataListener = (eventData) => {
      dataQueue.push(eventData);
    };
    const errorListener = (eventData) => {
      hasError = true;
      error = eventData.error;
    };
    const closeListener = () => {
      isComplete = true;
    };
    this.on(StreamEvent.Data, dataListener);
    this.on(StreamEvent.Error, errorListener);
    this.on(StreamEvent.Close, closeListener);
    try {
      while (!isComplete && !hasError) {
        if (dataQueue.length > 0) {
          yield dataQueue.shift();
        } else {
          await new Promise((resolve) => setTimeout(resolve, 10));
        }
      }
      if (hasError && error) {
        throw error;
      }
    } finally {
      this.off(StreamEvent.Data, dataListener);
      this.off(StreamEvent.Error, errorListener);
      this.off(StreamEvent.Close, closeListener);
    }
  }
};

// src/stream/stream_client.ts
var StreamClient = class {
  client;
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
       * Stream sampled Posts
       * Streams a 1% sample of public Posts in real-time.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async postsSample(options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "postsSample");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/sample/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream Portuguese Posts
       * Streams all public Portuguese-language Posts in real-time.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async postsFirehosePt(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "postsFirehosePt");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/firehose/stream/lang/pt";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream Japanese Posts
       * Streams all public Japanese-language Posts in real-time.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async postsFirehoseJa(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "postsFirehoseJa");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/firehose/stream/lang/ja";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream 10% sampled Posts
       * Streams a 10% sample of public Posts in real-time.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async postsSample10(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "postsSample10");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/sample10/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream Korean Posts
       * Streams all public Korean-language Posts in real-time.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async postsFirehoseKo(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "postsFirehoseKo");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/firehose/stream/lang/ko";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream Likes compliance data
       * Streams all compliance data related to Likes for Users.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async likesCompliance(options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "likesCompliance");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/likes/compliance/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream Posts compliance data
       * Streams all compliance data related to Posts.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async postsCompliance(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "postsCompliance");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/compliance/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream all Likes
       * Streams all public Likes in real-time.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async likesFirehose(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "likesFirehose");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime",
      "like_with_tweet_author.fields": "likeWithTweetAuthorFields",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      likeWithTweetAuthorFields = [],
      expansions = [],
      userFields = [],
      tweetFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/likes/firehose/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (likeWithTweetAuthorFields !== void 0 && likeWithTweetAuthorFields.length > 0) {
      params.append(
        "like_with_tweet_author.fields",
        likeWithTweetAuthorFields.join(",")
      );
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream English Posts
       * Streams all public English-language Posts in real-time.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async postsFirehoseEn(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "postsFirehoseEn");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/firehose/stream/lang/en";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream filtered Posts
       * Streams Posts in real-time matching the active rule set.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async posts(options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "posts");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/search/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream Users compliance data
       * Streams all compliance data related to Users.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async usersCompliance(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "usersCompliance");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/users/compliance/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream all Posts
       * Streams all public Posts in real-time.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async postsFirehose(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "postsFirehose");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime",
      "tweet.fields": "tweetFields",
      "media.fields": "mediaFields",
      "poll.fields": "pollFields",
      "user.fields": "userFields",
      "place.fields": "placeFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      tweetFields = [],
      expansions = [],
      mediaFields = [],
      pollFields = [],
      userFields = [],
      placeFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/firehose/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (mediaFields !== void 0 && mediaFields.length > 0) {
      params.append("media.fields", mediaFields.join(","));
    }
    if (pollFields !== void 0 && pollFields.length > 0) {
      params.append("poll.fields", pollFields.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (placeFields !== void 0 && placeFields.length > 0) {
      params.append("place.fields", placeFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream sampled Likes
       * Streams a 10% sample of public Likes in real-time.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @param partition The partition number.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async likesSample10(partition, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "likesSample10");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime",
      "like_with_tweet_author.fields": "likeWithTweetAuthorFields",
      "user.fields": "userFields",
      "tweet.fields": "tweetFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      likeWithTweetAuthorFields = [],
      expansions = [],
      userFields = [],
      tweetFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/likes/sample10/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (partition !== void 0) {
      params.append("partition", String(partition));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    if (likeWithTweetAuthorFields !== void 0 && likeWithTweetAuthorFields.length > 0) {
      params.append(
        "like_with_tweet_author.fields",
        likeWithTweetAuthorFields.join(",")
      );
    }
    if (expansions !== void 0 && expansions.length > 0) {
      params.append("expansions", expansions.join(","));
    }
    if (userFields !== void 0 && userFields.length > 0) {
      params.append("user.fields", userFields.join(","));
    }
    if (tweetFields !== void 0 && tweetFields.length > 0) {
      params.append("tweet.fields", tweetFields.join(","));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
       * Stream Post labels
       * Streams all labeling events applied to Posts.
       * 
       * Returns an event-driven stream that's easy to use.
       * Use .on() to listen for events like 'data', 'error', 'close'.
       * Also supports async iteration with for await...of.
  
  
  
       * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
       */
  async labelsCompliance(options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "labelsCompliance");
    const paramMappings = {
      backfill_minutes: "backfillMinutes",
      start_time: "startTime",
      end_time: "endTime"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      backfillMinutes = void 0,
      startTime = void 0,
      endTime = void 0,
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/label/stream";
    const params = new URLSearchParams();
    if (backfillMinutes !== void 0) {
      params.append("backfill_minutes", String(backfillMinutes));
    }
    if (startTime !== void 0) {
      params.append("start_time", String(startTime));
    }
    if (endTime !== void 0) {
      params.append("end_time", String(endTime));
    }
    const url = path + (params.toString() ? `?${params.toString()}` : "");
    const response = await this.client.request("GET", url, {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      signal,
      raw: true,
      // Get raw Response object for streaming
      timeout: 0,
      // Disable timeout for streaming requests
      ...requestOptions
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    if (!response.body) {
      throw new Error("Response body is not available for streaming");
    }
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }
  /**
     * Get stream rule counts
     * Retrieves the count of rules in the active rule set for the filtered stream.
     * 
     * @returns Promise with the API response
     */
  async getRuleCounts(options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "getRuleCounts");
    const paramMappings = {
      "rules_count.fields": "rulesCountFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      rulesCountFields = [],
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/search/stream/rules/counts";
    const params = new URLSearchParams();
    if (rulesCountFields !== void 0 && rulesCountFields.length > 0) {
      params.append("rules_count.fields", rulesCountFields.join(","));
    }
    const finalRequestOptions = {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      signal,
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get stream rules
     * Retrieves the active rule set or a subset of rules for the filtered stream.
     * 
     * @returns Promise with the API response
     */
  async getRules(options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "getRules");
    const paramMappings = {
      max_results: "maxResults",
      pagination_token: "paginationToken"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      ids = [],
      maxResults = void 0,
      paginationToken = void 0,
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/search/stream/rules";
    const params = new URLSearchParams();
    if (ids !== void 0 && ids.length > 0) {
      params.append("ids", ids.join(","));
    }
    if (maxResults !== void 0) {
      params.append("max_results", String(maxResults));
    }
    if (paginationToken !== void 0) {
      params.append("pagination_token", String(paginationToken));
    }
    const finalRequestOptions = {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      signal,
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Update stream rules
     * Adds or deletes rules from the active rule set for the filtered stream.
     * 
     * @returns Promise with the API response
     */
  async updateRules(body, options = {}) {
    const requiredAuthTypes = [];
    requiredAuthTypes.push("BearerToken");
    this.client.validateAuthentication(requiredAuthTypes, "updateRules");
    const paramMappings = {
      dry_run: "dryRun",
      delete_all: "deleteAll"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      dryRun = void 0,
      deleteAll = void 0,
      headers = {},
      signal,
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/tweets/search/stream/rules";
    const params = new URLSearchParams();
    if (dryRun !== void 0) {
      params.append("dry_run", String(dryRun));
    }
    if (deleteAll !== void 0) {
      params.append("delete_all", String(deleteAll));
    }
    const finalRequestOptions = {
      headers: {
        "Content-Type": "application/json",
        ...headers
      },
      signal,
      body: JSON.stringify(body),
      ...requestOptions
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/compliance/client.ts
var ComplianceClient = class {
  client;
  /**
     * Creates a new compliance client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get Compliance Jobs
     * Retrieves a list of Compliance Jobs filtered by job type and optional status.
  
  
  
     * @param type Type of Compliance Job to list.
  
  
  
     * @returns {Promise<GetJobsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getJobs(type, options = {}) {
    const paramMappings = {
      "compliance_job.fields": "complianceJobFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      status = void 0,
      complianceJobFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/compliance/jobs";
    const params = new URLSearchParams();
    if (type !== void 0) {
      params.append("type", String(type));
    }
    if (status !== void 0) {
      params.append("status", String(status));
    }
    if (complianceJobFields !== void 0 && complianceJobFields.length > 0) {
      params.append("compliance_job.fields", complianceJobFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Create Compliance Job
     * Creates a new Compliance Job for the specified job type.
  
  
  
     * @param body Request body
  
     * @returns {Promise<CreateJobsResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async createJobs(body) {
    let path = "/2/compliance/jobs";
    const params = new URLSearchParams();
    const finalRequestOptions = {
      body: JSON.stringify(body || {}),
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ]
      // No optional parameters, using empty request options
    };
    return this.client.request(
      "POST",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
  /**
     * Get Compliance Job by ID
     * Retrieves details of a specific Compliance Job by its ID.
  
  
     * @param id The ID of the Compliance Job to retrieve.
  
  
  
  
     * @returns {Promise<GetJobsByIdResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async getJobsById(id, options = {}) {
    const paramMappings = {
      "compliance_job.fields": "complianceJobFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      complianceJobFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/compliance/jobs/{id}";
    path = path.replace("{id}", encodeURIComponent(String(id)));
    const params = new URLSearchParams();
    if (complianceJobFields !== void 0 && complianceJobFields.length > 0) {
      params.append("compliance_job.fields", complianceJobFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/compliance/models.ts
var models_exports16 = {};

// src/usage/client.ts
var UsageClient = class {
  client;
  /**
     * Creates a new usage client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client) {
    this.client = client;
  }
  /**
     * Normalize options object to handle both camelCase and original API parameter names
     * Only accepts: proper camelCase (tweetFields) and original API format (tweet.fields)
     */
  _normalizeOptions(options, paramMappings) {
    if (!options || typeof options !== "object") {
      return options;
    }
    const normalized = { ...options };
    for (const [originalName, camelName] of Object.entries(paramMappings)) {
      if (originalName in normalized && !(camelName in normalized)) {
        normalized[camelName] = normalized[originalName];
        delete normalized[originalName];
      }
    }
    return normalized;
  }
  /**
     * Get usage
     * Retrieves usage statistics for Posts over a specified number of days.
  
  
  
     * @returns {Promise<GetResponse>} Promise resolving to the API response
     */
  // Overload 1: Default behavior (unwrapped response)
  async get(options = {}) {
    const paramMappings = {
      "usage.fields": "usageFields"
    };
    const normalizedOptions = this._normalizeOptions(
      options || {},
      paramMappings
    );
    const {
      days = void 0,
      usageFields = [],
      requestOptions = {}
    } = normalizedOptions;
    let path = "/2/usage/tweets";
    const params = new URLSearchParams();
    if (days !== void 0) {
      params.append("days", String(days));
    }
    if (usageFields !== void 0 && usageFields.length > 0) {
      params.append("usage.fields", usageFields.join(","));
    }
    const finalRequestOptions = {
      // Pass security requirements for smart auth selection
      security: [
        {
          BearerToken: []
        }
      ],
      ...requestOptions
    };
    return this.client.request(
      "GET",
      path + (params.toString() ? `?${params.toString()}` : ""),
      finalRequestOptions
    );
  }
};

// src/usage/models.ts
var models_exports17 = {};

// src/client.ts
var ApiError = class extends Error {
  status;
  statusText;
  headers;
  data;
  constructor(message, status, statusText, headers, data) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.statusText = statusText;
    this.headers = headers;
    this.data = data;
  }
};
var Client = class {
  /** Base URL for API requests */
  baseUrl;
  /** Bearer token for authentication */
  bearerToken;
  /** OAuth2 access token */
  accessToken;
  /** OAuth1 instance for authentication */
  oauth1;
  /** Headers for requests */
  headers;
  /** Request timeout in milliseconds */
  timeout;
  /** Whether to automatically retry failed requests */
  retry;
  /** Maximum number of retry attempts */
  maxRetries;
  /** HTTP client for making requests */
  httpClient = httpClient;
  /** activity client */
  activity;
  /** news client */
  news;
  /** connections client */
  connections;
  /** account activity client */
  accountActivity;
  /** spaces client */
  spaces;
  /** trends client */
  trends;
  /** media client */
  media;
  /** direct messages client */
  directMessages;
  /** posts client */
  posts;
  /** lists client */
  lists;
  /** community notes client */
  communityNotes;
  /** general client */
  general;
  /** webhooks client */
  webhooks;
  /** users client */
  users;
  /** communities client */
  communities;
  /** stream client */
  stream;
  /** compliance client */
  compliance;
  /** usage client */
  usage;
  /**
   * Creates a new X API client instance
   * 
   * @param config - Configuration options for the client
   * 
   * @example
   * ```typescript
   * // Bearer token authentication
   * const client = new Client({
   *   bearerToken: 'your-bearer-token'
   * });
   * 
   * // OAuth2 authentication
   * const client = new Client({
   *   accessToken: 'your-access-token'
   * });
   * 
   * // OAuth1 authentication
   * const client = new Client({
   *   oauth1: oauth1Instance
   * });
   * ```
   */
  constructor(config) {
    if (config && typeof config === "object" && config.accessToken && config.accessToken.accessToken && config.accessToken.accessTokenSecret) {
      this.oauth1 = config;
      this.baseUrl = "https://api.x.com";
    } else {
      const clientConfig = config;
      this.baseUrl = clientConfig.baseUrl || "https://api.x.com";
      this.bearerToken = clientConfig.bearerToken;
      this.accessToken = clientConfig.accessToken;
      this.oauth1 = clientConfig.oauth1;
    }
    this.timeout = config.timeout || 3e4;
    this.retry = config.retry ?? true;
    this.maxRetries = config.maxRetries || 3;
    const defaultHeaders = {
      "User-Agent": "xdk-typescript/0.2.1-beta",
      "Content-Type": "application/json",
      "Accept": "application/json",
      ...config.headers || {}
    };
    this.headers = httpClient.createHeaders(defaultHeaders);
    this.activity = new ActivityClient(this);
    this.news = new NewsClient(this);
    this.connections = new ConnectionsClient(this);
    this.accountActivity = new AccountActivityClient(this);
    this.spaces = new SpacesClient(this);
    this.trends = new TrendsClient(this);
    this.media = new MediaClient(this);
    this.directMessages = new DirectMessagesClient(this);
    this.posts = new PostsClient(this);
    this.lists = new ListsClient(this);
    this.communityNotes = new CommunityNotesClient(this);
    this.general = new GeneralClient(this);
    this.webhooks = new WebhooksClient(this);
    this.users = new UsersClient(this);
    this.communities = new CommunitiesClient(this);
    this.stream = new StreamClient(this);
    this.compliance = new ComplianceClient(this);
    this.usage = new UsageClient(this);
  }
  /**
   * Make an authenticated request to the X API
   * 
   * This method handles authentication, request formatting, and error handling
   * for all API requests. It automatically adds the appropriate authentication
   * headers based on the client configuration.
   * 
   * @param method - HTTP method (GET, POST, PUT, DELETE, etc.)
   * @param path - API endpoint path (e.g., '/2/users/by/username/username')
   * @param options - Request options including timeout, headers, and body
   * @returns Promise that resolves to the parsed response data
   * 
   * @example
   * ```typescript
   * // GET request
   * const user = await client.request('GET', '/2/users/by/username/username', {
   *   timeout: 5000
   * });
   * 
   * // POST request with body
   * const result = await client.request('POST', '/2/tweets', {
   *   body: JSON.stringify({ text: 'Hello World!' })
   * });
   * ```
   * 
   * @throws {ApiError} When the API returns an error response
   */
  async request(method, path, options = {}) {
    const url = `${this.baseUrl}${path}`;
    const headers = new Headers(this.headers);
    const selectedAuth = this.selectAuthMethod(method, options.security);
    if (selectedAuth === "bearer_token" && this.bearerToken) {
      headers.set("Authorization", `Bearer ${this.bearerToken}`);
    } else if (selectedAuth === "oauth2_user_context" && this.accessToken) {
      headers.set("Authorization", `Bearer ${this.accessToken}`);
    } else if (selectedAuth === "oauth1" && this.oauth1 && this.oauth1.accessToken) {
      try {
        const oauthHeader = await this.oauth1.buildRequestHeader(method, url, options.body || "");
        headers.set("Authorization", oauthHeader);
      } catch (error) {
        throw new Error(`Failed to build OAuth1 header: ${error instanceof Error ? error.message : "Unknown error"}`);
      }
    } else if (!selectedAuth) {
      const requiredSchemes = options.security ? options.security.flatMap((req) => Object.keys(req)) : [];
      if (requiredSchemes.length > 0) {
        this.validateAuthentication(requiredSchemes, path);
      }
    }
    if (options.headers) {
      Object.entries(options.headers).forEach(([key, value]) => {
        headers.set(key, value);
      });
    }
    try {
      const response = await this.httpClient.request(url, {
        method,
        headers,
        signal: options.signal,
        body: options.body,
        timeout: options.timeout !== void 0 ? options.timeout : this.timeout
      });
      if (!response.ok) {
        let errorData;
        try {
          errorData = await response.json();
        } catch {
          errorData = await response.text();
        }
        throw new ApiError(
          errorData && errorData.message ? errorData.message : `HTTP ${response.status}: ${response.statusText}`,
          response.status,
          response.statusText,
          response.headers,
          errorData
        );
      }
      if (options.raw) {
        return response;
      }
      let data;
      const contentType = response.headers.get("content-type");
      if (contentType && contentType.includes("application/json")) {
        data = await response.json();
      } else {
        data = await response.text();
      }
      return data;
    } catch (error) {
      if (error instanceof ApiError) {
        throw error;
      }
      throw new ApiError(
        error instanceof Error ? error.message : "Request failed",
        0,
        "NETWORK_ERROR",
        new Headers(),
        error
      );
    }
  }
  /**
   * Check if the OAuth2 token is expired
   */
  isTokenExpired() {
    return false;
  }
  /**
   * Refresh the OAuth2 token
   */
  async refreshToken() {
  }
  /**
   * Get the current authentication status
   */
  isAuthenticated() {
    return !!(this.bearerToken || this.accessToken || this.oauth1 && this.oauth1.accessToken);
  }
  /**
   * Map OpenAPI security scheme names to internal authentication types
   * @param securitySchemeName The security scheme name from OpenAPI
   * @returns Array of internal authentication types
   */
  mapSecuritySchemeToAuthTypes(securitySchemeName) {
    const schemeMapping = {
      "BearerToken": ["bearer_token"],
      // App-only OAuth2.0
      "OAuth2UserToken": ["oauth2_user_context"],
      // OAuth2.0 User Context
      "UserToken": ["oauth1"],
      // OAuth1.0a User Context
      // Fallback mappings for common variations
      "OAuth2": ["bearer_token", "oauth2_user_context"],
      "OAuth1": ["oauth1"],
      "Bearer": ["bearer_token"],
      "OAuth2User": ["oauth2_user_context"],
      "OAuth1User": ["oauth1"]
    };
    return schemeMapping[securitySchemeName] || [securitySchemeName.toLowerCase()];
  }
  /**
   * Select the best authentication method based on endpoint requirements and available credentials
   * 
   * Priority strategy:
   * 1. If endpoint only accepts one method, use that (if available)
   * 2. If endpoint accepts multiple methods:
   *    - For write operations (POST/PUT/DELETE): Prefer OAuth1 > OAuth2 User Token > Bearer Token
   *    - For read operations (GET): Prefer Bearer Token > OAuth2 User Token > OAuth1
   *    - This allows Bearer Token for read-only operations while using user context for writes
   * 
   * @param method HTTP method (GET, POST, etc.)
   * @param securityRequirements Security requirements from OpenAPI spec (array of security requirement objects)
   * @returns Selected auth method: 'bearer_token', 'oauth2_user_context', 'oauth1', or null if none available
   */
  selectAuthMethod(method, securityRequirements) {
    if (!securityRequirements || securityRequirements.length === 0) {
      if (this.bearerToken)
        return "bearer_token";
      if (this.accessToken)
        return "oauth2_user_context";
      if (this.oauth1 && this.oauth1.accessToken)
        return "oauth1";
      return null;
    }
    const acceptableSchemes = /* @__PURE__ */ new Set();
    for (const requirement of securityRequirements) {
      for (const schemeName of Object.keys(requirement)) {
        acceptableSchemes.add(schemeName);
      }
    }
    const availableAuth = {
      "BearerToken": !!this.bearerToken,
      "OAuth2UserToken": !!this.accessToken,
      "UserToken": !!(this.oauth1 && this.oauth1.accessToken)
    };
    if (acceptableSchemes.size === 1) {
      const scheme = Array.from(acceptableSchemes)[0];
      if (availableAuth[scheme]) {
        return this.mapSecuritySchemeToAuthTypes(scheme)[0];
      }
      return null;
    }
    const isWriteOperation = ["POST", "PUT", "DELETE", "PATCH"].includes(method.toUpperCase());
    if (isWriteOperation) {
      if (acceptableSchemes.has("UserToken") && availableAuth["UserToken"]) {
        return "oauth1";
      }
      if (acceptableSchemes.has("OAuth2UserToken") && availableAuth["OAuth2UserToken"]) {
        return "oauth2_user_context";
      }
      if (acceptableSchemes.has("BearerToken") && availableAuth["BearerToken"]) {
        return "bearer_token";
      }
    } else {
      if (acceptableSchemes.has("BearerToken") && availableAuth["BearerToken"]) {
        return "bearer_token";
      }
      if (acceptableSchemes.has("OAuth2UserToken") && availableAuth["OAuth2UserToken"]) {
        return "oauth2_user_context";
      }
      if (acceptableSchemes.has("UserToken") && availableAuth["UserToken"]) {
        return "oauth1";
      }
    }
    return null;
  }
  /**
   * Validate that the required authentication method is available
   * @param requiredAuthTypes Array of required authentication types (OpenAPI security scheme names)
   * @param operationName Name of the operation for error messages
   */
  validateAuthentication(requiredAuthTypes, operationName) {
    if (requiredAuthTypes.length === 0) {
      return;
    }
    const availableAuthTypes = [];
    if (this.bearerToken) {
      availableAuthTypes.push("bearer_token");
    }
    if (this.accessToken) {
      availableAuthTypes.push("oauth2_user_context");
    }
    if (this.oauth1 && this.oauth1.accessToken) {
      availableAuthTypes.push("oauth1");
    }
    const mappedRequiredTypes = requiredAuthTypes.flatMap(
      (scheme) => this.mapSecuritySchemeToAuthTypes(scheme)
    );
    const hasRequiredAuth = mappedRequiredTypes.some(
      (required) => availableAuthTypes.includes(required)
    );
    if (!hasRequiredAuth) {
      const availableStr = availableAuthTypes.length > 0 ? availableAuthTypes.join(", ") : "none";
      const requiredStr = requiredAuthTypes.join(", ");
      throw new Error(
        `Authentication required for ${operationName}. Required: ${requiredStr}. Available: ${availableStr}. Please configure the appropriate authentication method.`
      );
    }
  }
  /**
   * Get available authentication types
   */
  getAvailableAuthTypes() {
    const authTypes = [];
    if (this.bearerToken)
      authTypes.push("bearer_token");
    if (this.accessToken)
      authTypes.push("oauth2_user_context");
    if (this.oauth1 && this.oauth1.accessToken)
      authTypes.push("oauth1");
    return authTypes;
  }
};

// src/crypto_utils.ts
var CryptoUtils = class {
  /**
   * Generate HMAC-SHA1 signature
   * @param key Signing key
   * @param message Message to sign
   * @returns Base64 encoded signature
   */
  static async hmacSha1(key, message) {
    if (typeof process !== "undefined" && process.versions && process.versions.node) {
      try {
        return await this._nodeHmacSha1(key, message);
      } catch (error) {
        console.warn("Node.js crypto failed, falling back:", error);
      }
    }
    if (typeof crypto !== "undefined" && crypto.subtle) {
      try {
        return await this._webCryptoHmacSha1(key, message);
      } catch (error) {
        console.warn("Web Crypto API failed, falling back:", error);
      }
    }
    return this._polyfillHmacSha1(key, message);
  }
  /**
   * Node.js native HMAC-SHA1 implementation
   */
  static async _nodeHmacSha1(key, message) {
    const crypto2 = await import('crypto');
    const hmac = crypto2.createHmac("sha1", key);
    hmac.update(message);
    return hmac.digest("base64");
  }
  /**
   * Web Crypto API HMAC-SHA1 implementation
   */
  static async _webCryptoHmacSha1(key, message) {
    const keyBuffer = this._stringToArrayBuffer(key);
    const messageBuffer = this._stringToArrayBuffer(message);
    const cryptoKey = await crypto.subtle.importKey(
      "raw",
      keyBuffer,
      { name: "HMAC", hash: "SHA-1" },
      false,
      ["sign"]
    );
    const signature = await crypto.subtle.sign(
      "HMAC",
      cryptoKey,
      messageBuffer
    );
    return this._arrayBufferToBase64(signature);
  }
  /**
   * Polyfill HMAC-SHA1 implementation using pure JavaScript
   * This is a fallback that works everywhere but is slower
   */
  static _polyfillHmacSha1(key, message) {
    throw new Error(
      "HMAC-SHA1 polyfill not implemented. Please ensure Node.js crypto or Web Crypto API is available."
    );
  }
  /**
   * Convert string to ArrayBuffer
   */
  static _stringToArrayBuffer(str) {
    const buffer = new ArrayBuffer(str.length);
    const view = new Uint8Array(buffer);
    for (let i2 = 0; i2 < str.length; i2++) {
      view[i2] = str.charCodeAt(i2);
    }
    return buffer;
  }
  /**
   * Convert ArrayBuffer to base64 string
   */
  static _arrayBufferToBase64(buffer) {
    const bytes = new Uint8Array(buffer);
    let binary = "";
    for (let i2 = 0; i2 < bytes.byteLength; i2++) {
      binary += String.fromCharCode(bytes[i2]);
    }
    return btoa(binary);
  }
  /**
   * Generate a random nonce for OAuth
   * @param length Length of the nonce
   * @returns Random nonce string
   */
  static generateNonce(length = 32) {
    if (typeof crypto !== "undefined" && crypto.getRandomValues) {
      const array = new Uint8Array(length);
      crypto.getRandomValues(array);
      return Array.from(array, (byte) => byte.toString(16).padStart(2, "0")).join(
        ""
      );
    } else {
      let result = "";
      const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
      for (let i2 = 0; i2 < length; i2++) {
        result += characters.charAt(
          Math.floor(Math.random() * characters.length)
        );
      }
      return result;
    }
  }
  /**
   * Generate timestamp for OAuth
   * @returns Unix timestamp as string
   */
  static generateTimestamp() {
    return Math.floor(Date.now() / 1e3).toString();
  }
  /**
   * Generate a cryptographically secure random string for PKCE code verifier
   * @param length Length of the code verifier (43-128 characters recommended)
   * @returns Random code verifier string
   */
  static generateCodeVerifier(length = 128) {
    if (typeof crypto !== "undefined" && crypto.getRandomValues) {
      const array = new Uint8Array(length);
      crypto.getRandomValues(array);
      return this._base64UrlEncode(array);
    } else {
      const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~";
      let result = "";
      for (let i2 = 0; i2 < length; i2++) {
        result += characters.charAt(
          Math.floor(Math.random() * characters.length)
        );
      }
      return result;
    }
  }
  /**
   * Generate PKCE code challenge from code verifier
   * @param codeVerifier The code verifier string
   * @returns Base64url encoded SHA256 hash of the code verifier
   */
  static async generateCodeChallenge(codeVerifier) {
    if (typeof process !== "undefined" && process.versions && process.versions.node) {
      try {
        return await this._nodeSha256(codeVerifier);
      } catch (error) {
        console.warn("Node.js crypto failed for SHA256, falling back:", error);
      }
    }
    if (typeof crypto !== "undefined" && crypto.subtle) {
      try {
        return await this._webCryptoSha256(codeVerifier);
      } catch (error) {
        console.warn("Web Crypto API failed for SHA256, falling back:", error);
      }
    }
    return this._polyfillSha256(codeVerifier);
  }
  /**
   * Node.js native SHA256 implementation for PKCE
   */
  static async _nodeSha256(message) {
    const crypto2 = await import('crypto');
    const hash = crypto2.createHash("sha256");
    hash.update(message);
    const digest = hash.digest();
    return this._base64UrlEncode(digest);
  }
  /**
   * Web Crypto API SHA256 implementation for PKCE
   */
  static async _webCryptoSha256(message) {
    const messageBuffer = this._stringToArrayBuffer(message);
    const hashBuffer = await crypto.subtle.digest("SHA-256", messageBuffer);
    return this._base64UrlEncode(hashBuffer);
  }
  /**
   * Polyfill SHA256 implementation for PKCE
   * This is a fallback that works everywhere but is slower
   */
  static _polyfillSha256(message) {
    throw new Error(
      "SHA256 polyfill not implemented. Please ensure Node.js crypto or Web Crypto API is available."
    );
  }
  /**
   * Convert ArrayBuffer or Uint8Array to base64url encoding (RFC 7636)
   */
  static _base64UrlEncode(buffer) {
    const bytes = buffer instanceof Uint8Array ? buffer : new Uint8Array(buffer);
    let binary = "";
    for (let i2 = 0; i2 < bytes.byteLength; i2++) {
      binary += String.fromCharCode(bytes[i2]);
    }
    return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=/g, "");
  }
};
async function hmacSha1(key, message) {
  return CryptoUtils.hmacSha1(key, message);
}
function generateNonce(length = 32) {
  return CryptoUtils.generateNonce(length);
}
function generateTimestamp() {
  return CryptoUtils.generateTimestamp();
}
function generateCodeVerifier(length = 128) {
  return CryptoUtils.generateCodeVerifier(length);
}
async function generateCodeChallenge(codeVerifier) {
  return CryptoUtils.generateCodeChallenge(codeVerifier);
}

// src/oauth2_auth.ts
var OAuth2 = class {
  config;
  token;
  codeVerifier;
  codeChallenge;
  constructor(config) {
    this.config = {
      scope: ["tweet.read", "users.read"],
      ...config
    };
  }
  /**
   * Get the authorization URL
   * @param state Optional state parameter for security
   * @returns Authorization URL
   */
  async getAuthorizationUrl(state) {
    const params = new URLSearchParams({
      response_type: "code",
      client_id: this.config.clientId,
      redirect_uri: this.config.redirectUri,
      scope: this.config.scope?.join(" ") || "",
      state: state || ""
    });
    return `https://x.com/i/oauth2/authorize?${params.toString()}`;
  }
  /**
   * Exchange authorization code for tokens
   * @param code Authorization code from callback
   * @param codeVerifier Optional code verifier for PKCE
   * @returns Promise with OAuth2 token
   */
  async exchangeCode(code, codeVerifier) {
    const params = new URLSearchParams({
      grant_type: "authorization_code",
      code,
      redirect_uri: this.config.redirectUri
    });
    if (codeVerifier) {
      params.append("code_verifier", codeVerifier);
    }
    const headers = {
      "Content-Type": "application/x-www-form-urlencoded"
    };
    if (this.config.clientSecret) {
      const credentials = this._base64Encode(`${this.config.clientId}:${this.config.clientSecret}`);
      headers["Authorization"] = `Basic ${credentials}`;
    } else {
      params.append("client_id", this.config.clientId);
    }
    const response = await fetch("https://api.x.com/2/oauth2/token", {
      method: "POST",
      headers,
      body: params.toString()
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => response.text());
      throw new Error(`HTTP error! status: ${response.status}, body: ${JSON.stringify(errorData)}`);
    }
    const data = await response.json();
    this.token = {
      access_token: data.access_token,
      token_type: data.token_type,
      expires_in: data.expires_in,
      refresh_token: data.refresh_token,
      scope: data.scope
    };
    return this.token;
  }
  /**
   * Get the current token
   * @returns Current OAuth2 token if available
   */
  getToken() {
    return this.token;
  }
  /**
   * Get the current code verifier (for PKCE)
   * @returns Current code verifier if available
   */
  getCodeVerifier() {
    return this.codeVerifier;
  }
  /**
   * Manually set PKCE parameters
   * @param codeVerifier The code verifier to use
   * @param codeChallenge Optional code challenge (will be generated if not provided)
   */
  async setPkceParameters(codeVerifier, codeChallenge) {
    this.codeVerifier = codeVerifier;
    if (codeChallenge) {
      this.codeChallenge = codeChallenge;
    } else {
      this.codeChallenge = await generateCodeChallenge(codeVerifier);
    }
  }
  /**
   * Get the current code challenge (for PKCE)
   * @returns Current code challenge if available
   */
  getCodeChallenge() {
    return this.codeChallenge;
  }
  /**
   * Base64 encode a string (with fallback for environments without btoa)
   * @param str String to encode
   * @returns Base64 encoded string
   */
  _base64Encode(str) {
    if (typeof btoa !== "undefined") {
      return btoa(str);
    } else if (typeof Buffer !== "undefined") {
      return Buffer.from(str, "utf8").toString("base64");
    } else {
      const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
      let result = "";
      let i2 = 0;
      while (i2 < str.length) {
        const a = str.charCodeAt(i2++);
        const b = i2 < str.length ? str.charCodeAt(i2++) : 0;
        const c = i2 < str.length ? str.charCodeAt(i2++) : 0;
        const bitmap = a << 16 | b << 8 | c;
        result += chars.charAt(bitmap >> 18 & 63);
        result += chars.charAt(bitmap >> 12 & 63);
        result += i2 - 2 < str.length ? chars.charAt(bitmap >> 6 & 63) : "=";
        result += i2 - 1 < str.length ? chars.charAt(bitmap & 63) : "=";
      }
      return result;
    }
  }
};

// src/oauth1_auth.ts
var OAuth1 = class {
  config;
  requestToken;
  accessToken;
  constructor(config) {
    this.config = config;
    if (config.accessToken && config.accessTokenSecret) {
      this.accessToken = {
        accessToken: config.accessToken,
        accessTokenSecret: config.accessTokenSecret
      };
    }
  }
  /**
   * Get the authorization URL for OAuth1 flow
   * @param loginWithX Whether to use "Log in with X" flow
   * @returns Authorization URL
   */
  getAuthorizationUrl(loginWithX = false) {
    if (!this.requestToken) {
      throw new Error("Request token not obtained. Call getRequestToken() first.");
    }
    const baseUrl = loginWithX ? "https://x.com/i/oauth/authenticate" : "https://x.com/oauth/authorize";
    const params = new URLSearchParams({
      oauth_token: this.requestToken.oauthToken
    });
    return `${baseUrl}?${params.toString()}`;
  }
  /**
   * Get request token to start OAuth1 flow
   * @returns Promise with request token
   */
  async getRequestToken() {
    const url = "https://api.x.com/oauth/request_token";
    const params = new URLSearchParams({
      oauth_callback: this.config.callback
    });
    const response = await fetch(`${url}?${params.toString()}`, {
      method: "POST",
      headers: {
        "Authorization": await this._buildOAuthHeader("POST", url, params.toString())
      }
    });
    if (!response.ok) {
      throw new Error(`Failed to get request token: ${response.status} ${response.statusText}`);
    }
    const responseText = await response.text();
    const responseParams = new URLSearchParams(responseText);
    this.requestToken = {
      oauthToken: responseParams.get("oauth_token"),
      oauthTokenSecret: responseParams.get("oauth_token_secret")
    };
    return this.requestToken;
  }
  /**
   * Exchange verifier for access token
   * @param verifier OAuth verifier from callback or PIN
   * @returns Promise with access token
   */
  async getAccessToken(verifier) {
    if (!this.requestToken) {
      throw new Error("Request token not obtained. Call getRequestToken() first.");
    }
    const url = "https://api.x.com/oauth/access_token";
    const params = new URLSearchParams({
      oauth_token: this.requestToken.oauthToken,
      oauth_verifier: verifier
    });
    const response = await fetch(`${url}?${params.toString()}`, {
      method: "POST",
      headers: {
        "Authorization": await this._buildOAuthHeader("POST", url, params.toString())
      }
    });
    if (!response.ok) {
      throw new Error(`Failed to get access token: ${response.status} ${response.statusText}`);
    }
    const responseText = await response.text();
    const responseParams = new URLSearchParams(responseText);
    this.accessToken = {
      accessToken: responseParams.get("oauth_token"),
      accessTokenSecret: responseParams.get("oauth_token_secret")
    };
    return this.accessToken;
  }
  /**
   * Build OAuth1 authorization header
   * @param method HTTP method
   * @param url Request URL
   * @param body Request body
   * @returns Promise that resolves to OAuth1 authorization header string
   */
  async _buildOAuthHeader(method, url, body) {
    const timestamp = generateTimestamp();
    const nonce = generateNonce();
    const oauthParams = {
      oauth_consumer_key: this.config.apiKey,
      oauth_nonce: nonce,
      oauth_signature_method: "HMAC-SHA1",
      oauth_timestamp: timestamp,
      oauth_version: "1.0"
    };
    if (this.requestToken) {
      oauthParams["oauth_token"] = this.requestToken.oauthToken;
    }
    if (this.accessToken) {
      oauthParams["oauth_token"] = this.accessToken.accessToken;
    }
    const paramString = this._buildParamString(oauthParams, body);
    const signatureBase = `${method.toUpperCase()}&${this._encode(url)}&${this._encode(paramString)}`;
    const signingKey = `${this._encode(this.config.apiSecret)}&${this._encode(
      this.requestToken?.oauthTokenSecret || this.accessToken?.accessTokenSecret || ""
    )}`;
    const signature = await CryptoUtils.hmacSha1(signingKey, signatureBase);
    oauthParams["oauth_signature"] = signature;
    const headerParams = Object.entries(oauthParams).map(([key, value]) => `${key}="${this._encode(value)}"`).join(", ");
    return `OAuth ${headerParams}`;
  }
  /**
   * Build parameter string for OAuth signature
   * @param oauthParams OAuth parameters
   * @param body Request body
   * @returns Parameter string
   */
  _buildParamString(oauthParams, body) {
    const allParams = { ...oauthParams };
    if (body) {
      let isJson = false;
      try {
        JSON.parse(body);
        isJson = true;
      } catch {
        isJson = false;
      }
      if (!isJson) {
        try {
          const bodyParams = new URLSearchParams(body);
          bodyParams.forEach((value, key) => {
            allParams[key] = value;
          });
        } catch (error) {
          console.warn("Failed to parse body parameters:", error);
        }
      }
    }
    const sortedParams = Object.entries(allParams).sort(([a], [b]) => a.localeCompare(b));
    return sortedParams.map(([key, value]) => `${this._encode(key)}=${this._encode(value)}`).join("&");
  }
  /**
   * URL encode string according to OAuth1 specification
   * @param str String to encode
   * @returns Encoded string
   */
  _encode(str) {
    return encodeURIComponent(str).replace(/!/g, "%21").replace(/\*/g, "%2A").replace(/'/g, "%27").replace(/\(/g, "%28").replace(/\)/g, "%29").replace(/%7E/g, "~");
  }
  /**
   * Convenience method to start the OAuth1 flow
   * @param loginWithX Whether to use "Log in with X" flow
   * @returns Promise that resolves to the authorization URL
   */
  async startOAuthFlow(loginWithX = false) {
    await this.getRequestToken();
    return this.getAuthorizationUrl(loginWithX);
  }
  /**
   * Build OAuth1 authorization header for API requests
   * @param method HTTP method
   * @param url Request URL
   * @param body Request body
   * @returns Promise that resolves to OAuth1 authorization header string
   */
  async buildRequestHeader(method, url, body = "") {
    if (!this.accessToken) {
      throw new Error("Access token not available. Complete OAuth1 flow first.");
    }
    let urlWithoutQuery = url;
    let queryParams = "";
    try {
      const urlObj = new URL(url);
      if (urlObj.search) {
        queryParams = urlObj.search.substring(1);
        urlWithoutQuery = urlObj.origin + urlObj.pathname;
      }
    } catch (error) {
      console.warn("Failed to parse URL for OAuth1:", error);
    }
    let allParams = "";
    if (queryParams && body) {
      allParams = `${queryParams}&${body}`;
    } else if (queryParams) {
      allParams = queryParams;
    } else if (body) {
      allParams = body;
    }
    return this._buildOAuthHeader(method, urlWithoutQuery, allParams);
  }
};

// src/schemas.ts
var schemas_exports = {};

// src/stream/models.ts
var models_exports18 = {};

// src/paginator.ts
var Paginator = class _Paginator {
  fetchPage;
  currentToken;
  previousToken;
  hasMore = true;
  isDone = false;
  allItems = [];
  currentMeta;
  currentIncludes;
  currentErrors;
  rateLimitHit = false;
  /**
   * Creates a new paginator instance
   * 
   * @param fetchPage - Function that fetches a page of data given a pagination token
   */
  constructor(fetchPage) {
    this.fetchPage = fetchPage;
  }
  /**
   * Get all fetched items
   */
  get items() {
    return [...this.allItems];
  }
  /**
   * Get current pagination metadata
   */
  get meta() {
    return this.currentMeta;
  }
  /**
   * Get current includes data
   */
  get includes() {
    return this.currentIncludes;
  }
  /**
   * Get current errors
   */
  get errors() {
    return this.currentErrors;
  }
  /**
   * Check if pagination is done
   */
  get done() {
    return this.isDone || this.rateLimitHit;
  }
  /**
   * Check if rate limit was hit
   */
  get rateLimited() {
    return this.rateLimitHit;
  }
  /**
   * Fetch the next page and add items to current instance
   * 
   * This method fetches the next page of data and appends the items to the
   * current paginator instance. It updates the pagination state and metadata.
   * 
   * @example
   * ```typescript
   * const followers = await client.users.getFollowers('783214');
   * await followers.fetchNext(); // Fetch first page
   * console.log(followers.items.length); // Number of followers
   * 
   * if (!followers.done) {
   *   await followers.fetchNext(); // Fetch second page
   *   console.log(followers.items.length); // Total followers across pages
   * }
   * ```
   * 
   * @throws {Error} When the API request fails
   */
  async fetchNext() {
    if (this.done) {
      return;
    }
    try {
      const response = await this.fetchPage(this.currentToken);
      this.previousToken = this.currentToken;
      this.currentToken = response.meta?.next_token;
      this.hasMore = !!this.currentToken;
      this.isDone = !this.hasMore;
      if (response.data) {
        this.allItems.push(...response.data);
      }
      this.currentMeta = response.meta;
      this.currentIncludes = response.includes;
      this.currentErrors = response.errors;
    } catch (error) {
      if (error.status === 429 || error.message?.includes("rate limit")) {
        this.rateLimitHit = true;
      }
      throw error;
    }
  }
  /**
   * Get next page as a new instance
   * 
   * This method creates a new paginator instance that starts from the next page,
   * without affecting the current paginator's state.
   * 
   * @example
   * ```typescript
   * const followers = await client.users.getFollowers('783214');
   * await followers.fetchNext(); // Fetch first page
   * 
   * if (!followers.done) {
   *   const nextPage = await followers.next(); // Get next page as new instance
   *   console.log(followers.items.length); // Still first page
   *   console.log(nextPage.items.length); // Second page
   * }
   * ```
   * 
   * @returns New paginator instance for the next page
   */
  async next() {
    if (this.done) {
      return new _Paginator(this.fetchPage);
    }
    const nextPaginator = new _Paginator(this.fetchPage);
    nextPaginator.currentToken = this.currentToken;
    await nextPaginator.fetchNext();
    return nextPaginator;
  }
  /**
   * Fetch previous page (if supported)
   */
  async fetchPrevious() {
    if (!this.previousToken) {
      return;
    }
    try {
      const response = await this.fetchPage(this.previousToken);
      this.currentToken = this.previousToken;
      this.previousToken = response.meta?.previous_token;
      this.hasMore = !!this.currentToken;
      this.isDone = !this.hasMore;
      this.allItems = response.data || [];
      this.currentMeta = response.meta;
      this.currentIncludes = response.includes;
      this.currentErrors = response.errors;
    } catch (error) {
      if (error.status === 429 || error.message?.includes("rate limit")) {
        this.rateLimitHit = true;
      }
      throw error;
    }
  }
  /**
   * Get previous page as a new instance
   */
  async previous() {
    if (!this.previousToken) {
      return new _Paginator(this.fetchPage);
    }
    const prevPaginator = new _Paginator(this.fetchPage);
    prevPaginator.currentToken = this.previousToken;
    await prevPaginator.fetchNext();
    return prevPaginator;
  }
  /**
   * Fetch up to a specified number of additional items
   */
  async fetchLast(count) {
    let fetched = 0;
    while (!this.done && fetched < count) {
      const beforeCount = this.allItems.length;
      await this.fetchNext();
      const afterCount = this.allItems.length;
      fetched += afterCount - beforeCount;
    }
  }
  /**
   * Reset paginator to initial state
   */
  reset() {
    this.currentToken = void 0;
    this.previousToken = void 0;
    this.hasMore = true;
    this.isDone = false;
    this.allItems = [];
    this.currentMeta = void 0;
    this.currentIncludes = void 0;
    this.currentErrors = void 0;
    this.rateLimitHit = false;
  }
  /**
   * Iterator for all fetched items
   */
  *[Symbol.iterator]() {
    for (const item of this.allItems) {
      yield item;
    }
  }
  /**
   * Async iterator that fetches pages automatically
   */
  async *[Symbol.asyncIterator]() {
    let lastYieldedIndex = 0;
    for (let i2 = lastYieldedIndex; i2 < this.allItems.length; i2++) {
      yield this.allItems[i2];
    }
    lastYieldedIndex = this.allItems.length;
    while (!this.done) {
      await this.fetchNext();
      for (let i2 = lastYieldedIndex; i2 < this.allItems.length; i2++) {
        yield this.allItems[i2];
      }
      lastYieldedIndex = this.allItems.length;
    }
  }
};
var PostPaginator = class extends Paginator {
  get posts() {
    return this.items;
  }
};
var UserPaginator = class extends Paginator {
  get users() {
    return this.items;
  }
};
var EventPaginator = class extends Paginator {
  get events() {
    return this.items;
  }
};

// src/index.ts
if (typeof process !== "undefined" && process.versions && process.versions.node) {
  if (typeof globalThis.fetch === "undefined" || typeof globalThis.Headers === "undefined") {
    try {
      if (typeof globalThis.fetch === "function" && typeof globalThis.Headers === "function") {
      } else {
        const nodeFetch = (init_src(), __toCommonJS(src_exports));
        const { Headers: NodeHeaders } = nodeFetch;
        if (typeof globalThis.fetch === "undefined") {
          globalThis.fetch = nodeFetch.default || nodeFetch;
        }
        if (typeof globalThis.Headers === "undefined") {
          globalThis.Headers = NodeHeaders;
        }
      }
    } catch (error) {
      console.warn(
        "X API SDK: node-fetch not found. For Node.js environments, please install node-fetch:\nnpm install node-fetch\nOr upgrade to Node.js 18+ for native fetch support."
      );
    }
  }
}
/*! Bundled license information:

web-streams-polyfill/dist/ponyfill.es2018.js:
  (**
   * @license
   * web-streams-polyfill v3.3.3
   * Copyright 2024 Mattias Buelens, Diwank Singh Tomer and other contributors.
   * This code is released under the MIT license.
   * SPDX-License-Identifier: MIT
   *)

fetch-blob/index.js:
  (*! fetch-blob. MIT License. Jimmy Wärting <https://jimmy.warting.se/opensource> *)

formdata-polyfill/esm.min.js:
  (*! formdata-polyfill. MIT License. Jimmy Wärting <https://jimmy.warting.se/opensource> *)

node-domexception/index.js:
  (*! node-domexception. MIT License. Jimmy Wärting <https://jimmy.warting.se/opensource> *)
*/

export { models_exports4 as AccountActivity, AccountActivityClient, models_exports as Activity, ActivityClient, ApiError, Client, models_exports15 as Communities, CommunitiesClient, models_exports11 as CommunityNotes, CommunityNotesClient, models_exports16 as Compliance, ComplianceClient, models_exports3 as Connections, ConnectionsClient, CryptoUtils, models_exports8 as DirectMessages, DirectMessagesClient, EventPaginator, models_exports12 as General, GeneralClient, HttpClient, models_exports10 as Lists, ListsClient, models_exports7 as Media, MediaClient, models_exports2 as News, NewsClient, OAuth1, OAuth2, Paginator, PostPaginator, models_exports9 as Posts, PostsClient, schemas_exports as Schemas, models_exports5 as Spaces, SpacesClient, models_exports18 as Stream, StreamClient, models_exports6 as Trends, TrendsClient, models_exports17 as Usage, UsageClient, UserPaginator, models_exports14 as Users, UsersClient, models_exports13 as Webhooks, WebhooksClient, generateCodeChallenge, generateCodeVerifier, generateNonce, generateTimestamp, hmacSha1, httpClient };
//# sourceMappingURL=out.js.map
//# sourceMappingURL=index.js.map