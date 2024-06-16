import { Injectable } from "@nestjs/common";
import { OnEvent } from "@nestjs/event-emitter";
import { UserCreatedEvent } from "src/events/events";

@Injectable()
export class UserCreatedListener {
  
  @OnEvent('user.created')
  handleUserCreated(event: UserCreatedEvent) {
    console.log('User created event received:', event);
  }
}