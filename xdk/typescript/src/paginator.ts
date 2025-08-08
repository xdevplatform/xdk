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
}
/**
 * Paginator class for handling paginated responses
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