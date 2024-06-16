import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { EventEmitterModule } from '@nestjs/event-emitter';
import { UserService } from './users/user.service';
import { UserCreatedListener } from './listeners/user-created.listener';

@Module({
  imports: [
    EventEmitterModule.forRoot(),
  ],
  controllers: [AppController],
  providers: [AppService, UserService, UserCreatedListener],
})
export class AppModule {}
