/**
 * Models for communities operations
 */

/**
 * Response for search
 */
export interface SearchResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for getById
 */
export interface GetByIdResponse {
  /** A X Community is a curated group of Posts. */
  data: Record<string, any>;
  errors?: Array<any>;
}
