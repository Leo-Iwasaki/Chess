//
//  ChessPiece.swift
//  Chess
//
//  Created by Kaede Sugano on 22/12/2023.
//

import SwiftUI

struct ChessPiece: Identifiable {
    let id = UUID()
    var name: String
    var side: ChessSide
    var row: Int
    var column: Int
    
    init(name: String, side: ChessSide, row: Int, column: Int) {
        self.name = name
        self.side = side
        self.row = row
        self.column = column
    }
}

class MoveText: ObservableObject, Equatable, Hashable {
    @Published var texts: [String] = []
    
    static func == (lhs: MoveText, rhs: MoveText) -> Bool {
        lhs.texts == rhs.texts
    }
    
    func hash(into hasher: inout Hasher) {
        hasher.combine(texts)
    }
}
