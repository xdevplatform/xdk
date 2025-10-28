/**
 * Pagination utilities for the X API.
 */

/**
 * Paginated response interface
 */
export interface PaginatedResponse<T> {
    data: T[];
    meta?: {
        result_count?: number;
        next_token?: string;
        previous_token?: string;
    };
    includes?: Record<string, any>;
    errors?: Array<any>;
}

/**
 * Base paginator class for handling paginated responses
 */
export class Paginator<T> {
    private fetchPage: (token?: string) => Promise<PaginatedResponse<T>>;
    private currentToken?: string;
    private hasMore: boolean = true;

    constructor(fetchPage: (token?: string) => Promise<PaginatedResponse<T>>) {
        this.fetchPage = fetchPage;
    }

    /**
     * Get the next page of results
     */
    async next(): Promise<PaginatedResponse<T>> {
        if (!this.hasMore) {
            return { data: [] };
        }

        const response = await this.fetchPage(this.currentToken);
        this.currentToken = response.meta?.next_token;
        this.hasMore = !!this.currentToken;

        return response;
    }

    /**
     * Check if there are more pages
     */
    hasNextPage(): boolean {
        return this.hasMore;
    }

    /**
     * Get all remaining results
     */
    async *[Symbol.asyncIterator](): AsyncIterator<T> {
        while (this.hasMore) {
            const response = await this.next();
            for (const item of response.data) {
                yield item;
            }
        }
    }
}

/**
 * Twitter-specific paginator with rich functionality
 */
export class TwitterPaginator<T> {
    private fetchPage: (token?: string) => Promise<PaginatedResponse<T>>;
    private currentToken?: string;
    private previousToken?: string;
    private hasMore: boolean = true;
    private isDone: boolean = false;
    private allItems: T[] = [];
    private currentMeta?: any;
    private currentIncludes?: Record<string, any>;
    private currentErrors?: Array<any>;
    private rateLimitHit: boolean = false;

    constructor(fetchPage: (token?: string) => Promise<PaginatedResponse<T>>) {
        this.fetchPage = fetchPage;
    }

    /**
     * Get all fetched items
     */
    get items(): T[] {
        return [...this.allItems];
    }

    /**
     * Get current pagination metadata
     */
    get meta(): any {
        return this.currentMeta;
    }

    /**
     * Get current includes data
     */
    get includes(): Record<string, any> | undefined {
        return this.currentIncludes;
    }

    /**
     * Get current errors
     */
    get errors(): Array<any> | undefined {
        return this.currentErrors;
    }

    /**
     * Check if pagination is done
     */
    get done(): boolean {
        return this.isDone || this.rateLimitHit;
    }

    /**
     * Check if rate limit was hit
     */
    get rateLimited(): boolean {
        return this.rateLimitHit;
    }

    /**
     * Fetch the next page and add items to current instance
     */
    async fetchNext(): Promise<void> {
        if (this.done) {
            return;
        }

        try {
            const response = await this.fetchPage(this.currentToken);
            
            // Update tokens
            this.previousToken = this.currentToken;
            this.currentToken = response.meta?.next_token;
            
            // Update state
            this.hasMore = !!this.currentToken;
            this.isDone = !this.hasMore;
            
            // Add new items to collection
            if (response.data) {
                this.allItems.push(...response.data);
            }
            
            // Update metadata
            this.currentMeta = response.meta;
            this.currentIncludes = response.includes;
            this.currentErrors = response.errors;
            
        } catch (error: any) {
            // Check if it's a rate limit error
            if (error.status === 429 || error.message?.includes('rate limit')) {
                this.rateLimitHit = true;
            }
            throw error;
        }
    }

    /**
     * Get next page as a new instance
     */
    async next(): Promise<TwitterPaginator<T>> {
        if (this.done) {
            return new TwitterPaginator(this.fetchPage);
        }

        const nextPaginator = new TwitterPaginator(this.fetchPage);
        nextPaginator.currentToken = this.currentToken;
        await nextPaginator.fetchNext();
        return nextPaginator;
    }

    /**
     * Fetch previous page (if supported)
     */
    async fetchPrevious(): Promise<void> {
        if (!this.previousToken) {
            return;
        }

        try {
            const response = await this.fetchPage(this.previousToken);
            
            // Update tokens
            this.currentToken = this.previousToken;
            this.previousToken = response.meta?.previous_token;
            
            // Update state
            this.hasMore = !!this.currentToken;
            this.isDone = !this.hasMore;
            
            // Replace items with previous page items
            this.allItems = response.data || [];
            
            // Update metadata
            this.currentMeta = response.meta;
            this.currentIncludes = response.includes;
            this.currentErrors = response.errors;
            
        } catch (error: any) {
            if (error.status === 429 || error.message?.includes('rate limit')) {
                this.rateLimitHit = true;
            }
            throw error;
        }
    }

    /**
     * Get previous page as a new instance
     */
    async previous(): Promise<TwitterPaginator<T>> {
        if (!this.previousToken) {
            return new TwitterPaginator(this.fetchPage);
        }

        const prevPaginator = new TwitterPaginator(this.fetchPage);
        prevPaginator.currentToken = this.previousToken;
        await prevPaginator.fetchNext();
        return prevPaginator;
    }

    /**
     * Fetch up to a specified number of additional items
     */
    async fetchLast(count: number): Promise<void> {
        let fetched = 0;
        
        while (!this.done && fetched < count) {
            const beforeCount = this.allItems.length;
            await this.fetchNext();
            const afterCount = this.allItems.length;
            fetched += (afterCount - beforeCount);
        }
    }

    /**
     * Reset paginator to initial state
     */
    reset(): void {
        this.currentToken = undefined;
        this.previousToken = undefined;
        this.hasMore = true;
        this.isDone = false;
        this.allItems = [];
        this.currentMeta = undefined;
        this.currentIncludes = undefined;
        this.currentErrors = undefined;
        this.rateLimitHit = false;
    }

    /**
     * Iterator for all fetched items
     */
    *[Symbol.iterator](): Iterator<T> {
        for (const item of this.allItems) {
            yield item;
        }
    }

    /**
     * Async iterator that fetches pages automatically
     */
    async *[Symbol.asyncIterator](): AsyncIterator<T> {
        let lastYieldedIndex = 0;
        
        // First, yield all currently fetched items
        for (let i = lastYieldedIndex; i < this.allItems.length; i++) {
            yield this.allItems[i];
        }
        lastYieldedIndex = this.allItems.length;

        // Then continue fetching and yielding new items
        while (!this.done) {
            await this.fetchNext();
            
            // Yield only new items since last iteration
            for (let i = lastYieldedIndex; i < this.allItems.length; i++) {
                yield this.allItems[i];
            }
            lastYieldedIndex = this.allItems.length;
        }
    }
}

/**
 * Specialized paginators for different data types
 */

/**
 * Paginator for tweets
 */
export class TweetPaginator extends TwitterPaginator<any> {
    get tweets(): any[] {
        return this.items;
    }
}

/**
 * Paginator for users
 */
export class UserPaginator extends TwitterPaginator<any> {
    get users(): any[] {
        return this.items;
    }
}

/**
 * Paginator for lists
 */
export class ListPaginator extends TwitterPaginator<any> {
    get lists(): any[] {
        return this.items;
    }
}

/**
 * Paginator for IDs only
 */
export class IdPaginator extends TwitterPaginator<string> {
    get ids(): string[] {
        return this.items;
    }
}

/**
 * Paginator for welcome messages
 */
export class WelcomeMessagePaginator extends TwitterPaginator<any> {
    get welcomeMessages(): any[] {
        return this.items;
    }
}

/**
 * Paginator for events (like DM events)
 */
export class EventPaginator extends TwitterPaginator<any> {
    get events(): any[] {
        return this.items;
    }
} 