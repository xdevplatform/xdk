/**
 * Models for Communities operations
 */







/**
 * Response for search
 * 
 */
export interface CommunitiesSearchResponse {
    
    
    
    
    data?: Array<any>;
    
    
    
    errors?: Array<any>;
    
    
    
    meta?: Record<string, any>;
    
    
}









/**
 * Response for getById
 * 
 */
export interface CommunitiesGetByIdResponse {
    
    
    
    
    /** A X Community is a curated group of Posts. */
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}



 