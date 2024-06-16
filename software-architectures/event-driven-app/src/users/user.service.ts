import { Injectable } from "@nestjs/common";
import { EventEmitter2 } from "@nestjs/event-emitter";
import { UserCreatedEvent } from "src/events/events";

@Injectable()
export class UserService {
    constructor(private eventEmitter: EventEmitter2) {}

    createUser(userId: string) {
        // Create user logic
        console.log('User created:', userId);
        const event = new UserCreatedEvent(userId);
        console.log('User created event emitted:', event);
        this.eventEmitter.emit('user.created', event);
    }
}